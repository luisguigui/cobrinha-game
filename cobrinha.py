"""
CYBER-SNAKE.EXE — NEON OVERDRIVE
Desenvolvido por: LUIS GUILHERME G.B. E OTAVIO CESAR
"""

import customtkinter as ctk
import tkinter as tk
import random


# ============================================================
#  CONSTANTES
# ============================================================

CANVAS_W    = 800
CANVAS_H    = 600
CELL        = 20                          # tamanho de cada célula em px
COLS        = CANVAS_W // CELL            # 40 colunas
ROWS        = CANVAS_H // CELL            # 30 linhas

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


# ============================================================
#  ENTIDADE: PARTÍCULA
# ============================================================

class Particle:
    """Partícula de efeito visual com vida e movimento próprio."""

    DECAY = 0.04

    def __init__(self, canvas: tk.Canvas, x: float, y: float, color: str):
        self.canvas = canvas
        size    = random.randint(1, 4)
        self.id = canvas.create_oval(x, y, x + size, y + size, fill=color, outline="")
        self.vx = random.uniform(-5, 5)
        self.vy = random.uniform(-5, 5)
        self.life = 1.0

    def update(self) -> bool:
        """Move e envelhece a partícula. Retorna False quando deve ser removida."""
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
    """Classe principal: gerencia UI, lógica e renderização do Snake."""

    # --------------------------------------------------------
    #  INICIALIZAÇÃO
    # --------------------------------------------------------

    def __init__(self):
        super().__init__()
        self.title("CYBER-SNAKE.EXE - NEON OVERDRIVE")
        self.geometry("1150x750")
        self.configure(fg_color="#000000")

        # Estado do jogo
        self.snake          = list(SNAKE_START)
        self.direction      = "Right"
        self.next_direction = "Right"
        self.food           = (0, 0)
        self.score          = 0
        self.running        = False
        self.is_fullscreen  = False
        self.particles: list[Particle] = []

        # Seleção de modo
        self.selected_mode = tk.StringVar(value="Beta (Médio)")

        self._setup_ui()
        self._update_scenario()
        self._spawn_food()

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

        ctk.CTkLabel(sidebar, text="CYBER-SNAKE",
                     font=("Fixedsys", 32, "bold"),
                     text_color=COLOR_ACCENT).pack(pady=30)

        self.score_lbl = ctk.CTkLabel(sidebar, text="ENERGY: 0",
                                      font=("Consolas", 28, "bold"),
                                      text_color="white")
        self.score_lbl.pack(pady=10)

        for mode in MODES:
            ctk.CTkRadioButton(sidebar, text=mode,
                               variable=self.selected_mode, value=mode,
                               command=self._update_scenario,
                               fg_color=COLOR_ACCENT).pack(pady=8, padx=30, anchor="w")

        self.btn_start = ctk.CTkButton(sidebar, text="BOOT SYSTEM",
                                       font=("Impact", 20), fg_color="#1f538d",
                                       height=50, command=self._toggle_game)
        self.btn_start.pack(side="bottom", pady=40, padx=20, fill="x")

    def _build_canvas(self):
        # Frame colorido funciona como moldura neon ao redor do canvas
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
    #  CENÁRIO / MODO
    # --------------------------------------------------------

    def _current_mode(self) -> dict:
        return MODES[self.selected_mode.get()]

    def _update_scenario(self):
        cfg = self._current_mode()
        self.canvas.configure(bg=cfg["bg"])
        self.canvas_frame.configure(bg=cfg["head"])
        self._render()

    # --------------------------------------------------------
    #  CONTROLES
    # --------------------------------------------------------

    def _handle_input(self, event):
        direction = KEY_MAP.get(event.keysym.lower())
        if direction:
            self._change_dir(direction)

    def _change_dir(self, d: str):
        if d != OPPOSITES.get(self.direction):
            self.next_direction = d

    def _toggle_fullscreen(self, _event=None):
        self.is_fullscreen = not self.is_fullscreen
        self.attributes("-fullscreen", self.is_fullscreen)

    def _toggle_game(self):
        if not self.running:
            self.running = True
            self.btn_start.configure(text="PAUSE SYSTEM", fg_color="#333")
            self._game_loop()
        else:
            self.running = False
            self.btn_start.configure(text="RESUME", fg_color="#1f538d")

    # --------------------------------------------------------
    #  LOOP PRINCIPAL
    # --------------------------------------------------------

    def _game_loop(self):
        if not self.running:
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
            return  # game over já chamado dentro de _apply_bounds

        new_head = (hx, hy)
        if new_head in self.snake:
            self._game_over()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self._collect_food()
        else:
            self.snake.pop()

    def _apply_bounds(self, hx: int, hy: int, cfg: dict) -> tuple[int | None, int | None]:
        """Aplica wrapping ou game over nas bordas. Retorna (None, None) se colidiu."""
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
        self.score_lbl.configure(text=f"ENERGY: {self.score}")
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
        # Brilho externo
        self.canvas.create_rectangle(sx - 2, sy - 2, sx + CELL + 2, sy + CELL + 2,
                                     outline=cfg["head"], width=1, tags="game_obj")
        # Cabeça
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
        self.running = False
        self.canvas.configure(bg="#220000")
        self.canvas.create_text(CANVAS_W // 2, CANVAS_H // 2,
                                text="SYSTEM CRASH",
                                font=("Fixedsys", 60, "bold"),
                                fill="white", tags="game_obj")
        self.btn_start.configure(text="REBOOT SYSTEM", fg_color="#880000")
        self._reset_state()

    def _reset_state(self):
        self.snake          = list(SNAKE_START)
        self.direction      = "Right"
        self.next_direction = "Right"
        self.score          = 0
        self.score_lbl.configure(text="ENERGY: 0")
        self.particles.clear()
        self._spawn_food()


# ============================================================
#  ENTRADA
# ============================================================

if __name__ == "__main__":
    CyberSnake().mainloop()