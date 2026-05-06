"""
CYBER-SNAKE.EXE — NEON OVERDRIVE
Desenvolvido por: LUIS GUILHERME G.B. E OTAVIO CESAR
"""

import customtkinter as ctk
import tkinter as tk
import random
import json
import os

# ============================================================
#  CONSTANTES
# ============================================================

CANVAS_W    = 800
CANVAS_H    = 600
CELL        = 20
COLS        = CANVAS_W // CELL
ROWS        = CANVAS_H // CELL

COLOR_SIDEBAR = "#050505"
COLOR_ACCENT  = "#00F2FF"

SNAKE_START = [(100, 100), (80, 100), (60, 100)]

OPPOSITES = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}

KEY_MAP = {
    "up": "Up",    "w": "Up",
    "down": "Down","s": "Down",
    "left": "Left","a": "Left",
    "right": "Right", "d": "Right",
}

MODES: dict[str, dict] = {
    "Estável (Fácil)": {
        "speed": 110, "bg": "#0a150a",
        "head": "#00FF41", "tail": "#005500",
        "food": "#FFFFFF", "wall_kill": False,
    },
    "Beta (Médio)": {
        "speed": 85, "bg": "#0a0a15",
        "head": "#00F2FF", "tail": "#003366",
        "food": "#FF0055", "wall_kill": True,
    },
    "Sobrecarga (Difícil)": {
        "speed": 60, "bg": "#150a0a",
        "head": "#FF9500", "tail": "#663300",
        "food": "#FFEE00", "wall_kill": True,
    },
    "CRÍTICO (Expert)": {
        "speed": 40, "bg": "#1a0000",
        "head": "#FF0000", "tail": "#330000",
        "food": "#FF00FF", "wall_kill": True,
    },
}

SAVE_FILE = "snake_score.json"

# ============================================================
#  ENTIDADE: PARTÍCULA
# ============================================================

class Particle:
    DECAY = 0.04

    def __init__(self, canvas: tk.Canvas, x: float, y: float, color: str):
        self.canvas = canvas
        size    = random.randint(1, 4)
        self.id = canvas.create_oval(x, y, x + size, y + size, fill=color, outline="")
        self.vx = random.uniform(-5, 5)
        self.vy = random.uniform(-5, 5)
        self.life = 1.0

    def update(self) -> bool:
        self.canvas.move(self.id, self.vx, self.vy)
        self.life -= self.DECAY
        if self.life <= 0:
            self.canvas.delete(self.id)
            return False
        return True


# ============================================================
#  JOGO PRINCIPAL
# ============================================================

class CyberSnake(ctk.CTk):

    # --------------------------------------------------------
    #  INICIALIZAÇÃO
    # --------------------------------------------------------

    def __init__(self):
        super().__init__()
        self.title("CYBER-SNAKE.EXE - NEON OVERDRIVE")
        self.geometry("1150x750")
        self.configure(fg_color="#000000")

        # Estado: "menu" | "playing" | "paused" | "over"
        # Alterado de self.state para self.game_state para evitar conflito
        self.game_state     = "menu" 
        self.snake          = list(SNAKE_START)
        self.direction      = "Right"
        self.next_direction = "Right"
        self.food           = (0, 0)
        self.score          = 0
        self.high_score     = self._load_highscore()
        self.is_fullscreen  = False
        self.particles: list[Particle] = []

        self.selected_mode = tk.StringVar(value="Beta (Médio)")

        self._setup_ui()
        self._spawn_food()
        self._draw_menu()

    # --------------------------------------------------------
    #  PERSISTÊNCIA
    # --------------------------------------------------------

    def _load_highscore(self) -> int:
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, "r") as f:
                    return json.load(f).get("hs", 0)
            except Exception:
                return 0
        return 0

    def _save_highscore(self):
        with open(SAVE_FILE, "w") as f:
            json.dump({"hs": self.high_score}, f)

    # --------------------------------------------------------
    #  INTERFACE (UI)
    # --------------------------------------------------------

    def _setup_ui(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self._build_sidebar()
        self._build_canvas()
        self._bind_keys()

    def _build_sidebar(self):
        sidebar = ctk.CTkFrame(self, width=280, corner_radius=0, fg_color=COLOR_SIDEBAR)
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_propagate(False)

        ctk.CTkLabel(sidebar, text="CYBER-SNAKE",
                     font=("Fixedsys", 32, "bold"),
                     text_color=COLOR_ACCENT).pack(pady=(30, 5))

        ctk.CTkLabel(sidebar, text="NEON OVERDRIVE",
                     font=("Consolas", 12),
                     text_color="#555555").pack(pady=(0, 20))

        # Score e Record
        score_frame = ctk.CTkFrame(sidebar, fg_color="#0d0d0d", corner_radius=10)
        score_frame.pack(padx=20, pady=(0, 10), fill="x")

        ctk.CTkLabel(score_frame, text="ENERGY",
                     font=("Consolas", 11), text_color="#555555").pack(pady=(8, 0))
        self.score_lbl = ctk.CTkLabel(score_frame, text="0",
                                      font=("Consolas", 36, "bold"),
                                      text_color="white")
        self.score_lbl.pack()

        ctk.CTkLabel(score_frame, text="RECORD",
                     font=("Consolas", 11), text_color="#555555").pack(pady=(4, 0))
        self.hs_lbl = ctk.CTkLabel(score_frame, text=str(self.high_score),
                                   font=("Consolas", 18, "bold"),
                                   text_color="#ffff00")
        self.hs_lbl.pack(pady=(0, 8))

        # Modos
        ctk.CTkLabel(sidebar, text="── MODO ──",
                     font=("Consolas", 11), text_color="#444444").pack(pady=(10, 5))

        for mode in MODES:
            ctk.CTkRadioButton(sidebar, text=mode,
                               variable=self.selected_mode, value=mode,
 command=self._on_mode_change, fg_color=COLOR_ACCENT, hover_color="#007a88").pack(pady=5, padx=30, anchor="w")

        # Botão principal
        self.btn_start = ctk.CTkButton(sidebar, text="▶  BOOT SYSTEM", font=("Impact", 18), fg_color="#1f538d", hover_color="#2a6fbb", height=50, command=self._toggle_game)
        self.btn_start.pack(side="bottom", pady=(0, 16), padx=20, fill="x")

        # Dica de teclas
        ctk.CTkLabel(sidebar, text="P = Pause   M = Menu   F11 = FullScreen", font=("Consolas", 9), text_color="#333333", wraplength=240).pack(side="bottom", pady=(0, 4))

    def _build_canvas(self):
        self.canvas_frame = tk.Frame(self, bg=COLOR_ACCENT, padx=3, pady=3)
        self.canvas_frame.grid(row=0, column=1, padx=40, pady=40)

        self.canvas = tk.Canvas(self.canvas_frame,
                                width=CANVAS_W, height=CANVAS_H,
                                highlightthickness=0, bd=0)
        self.canvas.pack()

    def _bind_keys(self):
        self.bind("<KeyPress>", self._handle_input)
        self.bind("<F11>",      self._toggle_fullscreen)

    # --------------------------------------------------------
    #  TELAS DE ESTADO
    # --------------------------------------------------------

    def _draw_menu(self):
        cfg = self._current_mode()
        self.canvas.delete("all")
        self.canvas.configure(bg=cfg["bg"])
        self.canvas_frame.configure(bg=cfg["head"])

        self._draw_grid()

        # Título
        self.canvas.create_text(CANVAS_W // 2, 100,
                                text="CYBER-SNAKE.EXE",
                                font=("Fixedsys", 46, "bold"),
                                fill=cfg["head"])
        self.canvas.create_text(CANVAS_W // 2, 148,
                                text="NEON  OVERDRIVE",
                                font=("Fixedsys", 18),
                                fill="#ffffff")

        # Linha separadora
        self.canvas.create_line(CANVAS_W // 2 - 220, 170,
                                CANVAS_W // 2 + 220, 170,
                                fill=cfg["head"], width=2)

        # Recorde
        self.canvas.create_text(CANVAS_W // 2, 195,
                                text=f"★  RECORDE: {self.high_score}  ★",
                                font=("Consolas", 16, "bold"),
                                fill="#ffff00")

        # Modo selecionado
        self.canvas.create_text(CANVAS_W // 2, 228,
                                text=f"MODO ATIVO → {self.selected_mode.get()}",
                                font=("Consolas", 12),
                                fill=cfg["head"])

        # Caixas de controles
        controls = [
            ("WASD / SETAS", "Mover a cobra"),
            ("ESPAÇO / ENTER", "Iniciar jogo"),
            ("P", "Pausar / Retomar"),
            ("M", "Voltar ao menu"),
            ("F11", "Tela cheia"),
        ]
        cx = CANVAS_W // 2
        y = 275
        self.canvas.create_text(cx, y, text="CONTROLES",
                                font=("Fixedsys", 14), fill=cfg["head"])
        y += 10
        self.canvas.create_line(cx - 120, y + 8, cx + 120, y + 8,
                                fill="#333333", width=1)
        for key, desc in controls:
            y += 30
            self.canvas.create_text(cx - 10, y, text=key,
                                    font=("Consolas", 12, "bold"),
                                    fill="white", anchor="e")
            self.canvas.create_text(cx + 10, y, text=f"→ {desc}",
                                    font=("Consolas", 12),
                                    fill="#888888", anchor="w")

        # Botão de start estilizado
        by = CANVAS_H - 60
        self.canvas.create_rectangle(cx - 180, by - 22, cx + 180, by + 22,
                                     outline=cfg["head"], width=2, fill="#0a0a0a")
        self.canvas.create_text(cx, by,
                                text="▶  PRESSIONE ESPAÇO PARA INICIAR",
                                font=("Consolas", 13, "bold"),
                                fill=cfg["head"])

    def _draw_pause_overlay(self):
        cfg = self._current_mode()
        cx, cy = CANVAS_W // 2, CANVAS_H // 2

        self.canvas.create_rectangle(0, 0, CANVAS_W, CANVAS_H,
                                     fill="#000000", stipple="gray50",
                                     tags="overlay")
        self.canvas.create_rectangle(cx - 220, cy - 80, cx + 220, cy + 90,
                                     fill="#0a0a0a", outline=cfg["head"],
                                     width=2, tags="overlay")
        self.canvas.create_text(cx, cy - 45,
                                text="⏸  SISTEMA PAUSADO",
                                font=("Fixedsys", 28, "bold"),
                                fill=cfg["head"], tags="overlay")
        self.canvas.create_line(cx - 180, cy - 10, cx + 180, cy - 10,
                                fill="#333333", tags="overlay")
        self.canvas.create_text(cx, cy + 20,
                                text="P   →   Retomar",
                                font=("Consolas", 15), fill="white", tags="overlay")
        self.canvas.create_text(cx, cy + 50,
                                text="M   →   Menu Principal",
                                font=("Consolas", 14), fill="#777777", tags="overlay")

    def _draw_game_over(self):
        cfg = self._current_mode()
        cx, cy = CANVAS_W // 2, CANVAS_H // 2

        self.canvas.configure(bg="#220000")
        self.canvas.create_rectangle(0, 0, CANVAS_W, CANVAS_H,
                                     fill="#000000", stipple="gray50",
                                     tags="game_obj")

        # Caixa central
        self.canvas.create_rectangle(cx - 260, cy - 110, cx + 260, cy + 120,
                                     fill="#0d0000", outline="#FF0000",
                                     width=2, tags="game_obj")

        self.canvas.create_text(cx, cy - 75,
                                text="SYSTEM CRASH",
                                font=("Fixedsys", 44, "bold"),
                                fill="#FF0000", tags="game_obj")

        self.canvas.create_line(cx - 220, cy - 40, cx + 220, cy - 40,
                                fill="#440000", tags="game_obj")

        self.canvas.create_text(cx, cy - 10,
                                text=f"SCORE:  {self.score}",
                                font=("Consolas", 24, "bold"),
                                fill="white", tags="game_obj")

        new_record = self.score > 0 and self.score == self.high_score
        if new_record:
            self.canvas.create_text(cx, cy + 28,
                                    text="★★  NOVO RECORDE!  ★★",
                                    font=("Fixedsys", 18, "bold"),
                                    fill="#ffff00", tags="game_obj")
        else:
            self.canvas.create_text(cx, cy + 28,
                                    text=f"RECORDE:  {self.high_score}",
                                    font=("Consolas", 16),
                                    fill="#888800", tags="game_obj")

        self.canvas.create_text(cx, cy + 80,
                                text="ESPAÇO → Reiniciar     M → Menu",
                                font=("Consolas", 13),
                                fill=cfg["head"], tags="game_obj")

    # --------------------------------------------------------
    #  CONTROLES E ESTADO
    # --------------------------------------------------------

    def _on_mode_change(self):
        if self.game_state == "menu":
            self._draw_menu()

    def _handle_input(self, event):
        key = event.keysym.lower()

        if self.game_state == "menu":
            if key in ("space", "return"):
                self._start_game()

        elif self.game_state == "playing":
            direction = KEY_MAP.get(key)
            if direction:
                self._change_dir(direction)
            elif key == "p":
                self._pause_game()
            elif key == "m":
                self._go_to_menu()

        elif self.game_state == "paused":
            if key == "p":
                self._resume_game()
            elif key == "m":
                self._go_to_menu()

        elif self.game_state == "over":
            if key in ("space", "return", "r"):
                self._start_game()
            elif key == "m":
                self._go_to_menu()

    def _toggle_game(self):
        if   self.game_state == "menu":    self._start_game()
        elif self.game_state == "playing": self._pause_game()
        elif self.game_state == "paused":  self._resume_game()
        elif self.game_state == "over":    self._start_game()

    def _start_game(self):
        self._reset_state()
        self.game_state = "playing"
        self.btn_start.configure(text="⏸  PAUSE SYSTEM", fg_color="#333333")
        self._update_scenario()
        self._game_loop()

    def _pause_game(self):
        self.game_state = "paused"
        self.btn_start.configure(text="▶  RETOMAR", fg_color="#1f538d")
        self._render()
        self._draw_pause_overlay()

    def _resume_game(self):
        self.game_state = "playing"
        self.btn_start.configure(text="⏸  PAUSE SYSTEM", fg_color="#333333")
        self._game_loop()

    def _go_to_menu(self):
        self.game_state = "menu"
        self.btn_start.configure(text="▶  BOOT SYSTEM", fg_color="#1f538d")
        self._reset_state()
        self._draw_menu()

    def _change_dir(self, d: str):
        if d != OPPOSITES.get(self.direction):
            self.next_direction = d

    def _toggle_fullscreen(self, _=None):
        self.is_fullscreen = not self.is_fullscreen
        self.attributes("-fullscreen", self.is_fullscreen)

    # --------------------------------------------------------
    #  CENÁRIO / MODO
    # --------------------------------------------------------

    def _current_mode(self) -> dict:
        return MODES[self.selected_mode.get()]

    def _update_scenario(self):
        cfg = self._current_mode()
        self.canvas.configure(bg=cfg["bg"])
        self.canvas_frame.configure(bg=cfg["head"])

    # --------------------------------------------------------
    #  LOOP PRINCIPAL
    # --------------------------------------------------------

    def _game_loop(self):
        if self.game_state != "playing":
            return
        cfg = self._current_mode()
        self._move_snake(cfg)
        self._update_particles()
        self._render()
        self.after(cfg["speed"], self._game_loop)

    # --------------------------------------------------------
    #  LÓGICA DA COBRA
    # --------------------------------------------------------

    def _move_snake(self, cfg: dict):
        self.direction = self.next_direction
        hx, hy = self.snake[0]

        if   self.direction == "Up":    hy -= CELL
        elif self.direction == "Down":  hy += CELL
        elif self.direction == "Left":  hx -= CELL
        elif self.direction == "Right": hx += CELL

        hx, hy = self._apply_bounds(hx, hy, cfg)
        if hx is None:
            return

        new_head = (hx, hy)
        if new_head in self.snake:
            self._game_over()
            return

        self.snake.insert(0, new_head)
        if new_head == self.food:
            self._collect_food()
        else:
            self.snake.pop()

    def _apply_bounds(self, hx: int, hy: int, cfg: dict):
        if cfg["wall_kill"]:
            if hx < 0 or hx >= CANVAS_W or hy < 0 or hy >= CANVAS_H:
                self._game_over()
                return None, None
        else:
            hx = hx % CANVAS_W
            hy = hy % CANVAS_H
        return hx, hy

    def _collect_food(self):
        self.score += 10
        self.score_lbl.configure(text=str(self.score))
        self._spawn_food()

    def _spawn_food(self):
        snake_set = set(self.snake)
        while True:
            x = random.randint(0, COLS - 1) * CELL
            y = random.randint(0, ROWS - 1) * CELL
            if (x, y) not in snake_set:
                self.food = (x, y)
                break

    # --------------------------------------------------------
    #  PARTÍCULAS
    # --------------------------------------------------------

    def _update_particles(self):
        self.particles = [p for p in self.particles if p.update()]

    def _spawn_particles(self, x: float, y: float, color: str, count: int = 8):
        for _ in range(count):
            self.particles.append(Particle(self.canvas, x, y, color))

    # --------------------------------------------------------
    #  RENDERIZAÇÃO
    # --------------------------------------------------------

    def _render(self):
        self.canvas.delete("game_obj")
        self.canvas.delete("grid")
        self.canvas.delete("overlay")
        cfg = self._current_mode()
        self._draw_grid()
        self._draw_scanlines()
        self._draw_food(cfg)
        self._draw_snake(cfg)

    def _draw_grid(self):
        for x in range(0, CANVAS_W, CELL):
            self.canvas.create_line(x, 0, x, CANVAS_H,
                                    fill="#ffffff", stipple="gray12", tags="grid")
        for y in range(0, CANVAS_H, CELL):
            self.canvas.create_line(0, y, CANVAS_W, y,
                                    fill="#ffffff", stipple="gray12", tags="grid")

    def _draw_scanlines(self):
        for i in range(0, CANVAS_H, 4):
            self.canvas.create_line(0, i, CANVAS_W, i,
                                    fill="#000000", stipple="gray25", tags="game_obj")

    def _draw_food(self, cfg: dict):
        fx, fy = self.food
        self.canvas.create_oval(fx, fy, fx + CELL, fy + CELL,
                                fill="", outline=cfg["food"], width=2, tags="game_obj")
        self.canvas.create_oval(fx + 6, fy + 6, fx + 14, fy + 14,
                                fill="white", tags="game_obj")

    def _draw_snake(self, cfg: dict):
        for i, (sx, sy) in enumerate(self.snake):
            if i == 0:
                self._draw_head(sx, sy, cfg)
            else:
                self._draw_segment(sx, sy, i, cfg)

    def _draw_head(self, sx: int, sy: int, cfg: dict):
        self.canvas.create_rectangle(sx - 2, sy - 2, sx + CELL + 2, sy + CELL + 2,
                                     outline=cfg["head"], width=1, tags="game_obj")
        self.canvas.create_rectangle(sx, sy, sx + CELL, sy + CELL,
                                     fill=cfg["head"], outline="white", tags="game_obj")

    def _draw_segment(self, sx: int, sy: int, index: int, cfg: dict):
        shrink = min(index, 8)
        offset = shrink / 2
        self.canvas.create_rectangle(
            sx + offset,        sy + offset,
            sx + CELL - offset, sy + CELL - offset,
            fill=cfg["tail"], outline=cfg["bg"], tags="game_obj"
        )

    # --------------------------------------------------------
    #  GAME OVER
    # --------------------------------------------------------

    def _game_over(self):
        self.game_state = "over"

        if self.score > self.high_score:
            self.high_score = self.score
            self.hs_lbl.configure(text=str(self.high_score))
            self._save_highscore()

        self.btn_start.configure(text="⟳  REBOOT SYSTEM", fg_color="#880000")
        self._render()
        self._draw_game_over()
        self._reset_state()

    def _reset_state(self):
        self.snake          = list(SNAKE_START)
        self.direction      = "Right"
        self.next_direction = "Right"
        self.score          = 0
        self.score_lbl.configure(text="0")
        self.particles.clear()
        self._spawn_food()


# ============================================================
#  ENTRADA
# ============================================================

if __name__ == "__main__":
    CyberSnake().mainloop()