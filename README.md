# 🐍 CYBER-SNAKE.EXE — NEON OVERDRIVE

> Um jogo Snake futurista desenvolvido em Python com CustomTkinter. Apresenta estética cyberpunk/neon com 4 modos de dificuldade progressivos, sistema de partículas para efeitos visuais, grid interativo e mecânicas de jogo polidas. Desenvolvido em colaboração com Otávio César.

[![Python](https://img.shields.io/badge/python-3.7+-3776ab.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/CustomTkinter-Latest-blue.svg)](https://github.com/TomSchimansky/CustomTkinter)
[![Game](https://img.shields.io/badge/Game-Snake%20Arcade-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-Production-brightgreen.svg)]()
[![Neon](https://img.shields.io/badge/Aesthetic-Neon%20Cyberpunk-ff00ff.svg)]()

<div align="center">

**[🚀 Instalação](#-instalação-e-execução) • [🎮 Como Jogar](#-como-jogar) • [📖 Documentação](#-arquitetura-e-estrutura) • [🎨 Modos](#-modos-de-dificuldade) • [⚙️ Mecânicas](#️-mecânicas-do-jogo)**

</div>

---

## 🌟 Visão Geral

**CYBER-SNAKE.EXE** é uma reinterpretação moderna e envolvente do clássico jogo Snake. Com **estética neon cyberpunk**, **4 modos de dificuldade** com progressão épica, **sistema de partículas** para efeitos visuales e **mecânicas polidas**, oferece uma experiência retro-futurista irresistível.

### ✨ Destaques Principais

- 🎨 **Estética Neon Cyberpunk**: Design visual impressionante com cores vibrantes
- 🎮 **4 Modos de Dificuldade**: Fácil, Médio, Difícil, Expert (CRÍTICO)
- ⚡ **Velocidade Progressiva**: De 110ms (fácil) até 40ms (expert)
- 🌊 **Sistema de Partículas**: Efeitos visuais dinâmicos ao comer comida
- 🔳 **Grid Interativo**: Fundo com grid estilo retro-computador
- 🎯 **Scanlines**: Efeito de tela CRT vintage
- 📊 **Score System**: Contagem de energia (pontos)
- 🔀 **Wrapping ou Paredes**: Modo fácil permite passar pelas bordas, outros causam game over
- ⌨️ **Controles WASD/Setas**: Múltiplas opções de entrada
- 🖥️ **Fullscreen (F11)**: Modo tela cheia imersivo

---

## 🎮 Como Jogar

### 🕹️ Controles

| Entrada | Ação |
|---------|------|
| **⬆️ UP / W** | Mover cobra para cima |
| **⬇️ DOWN / S** | Mover cobra para baixo |
| **⬅️ LEFT / A** | Mover cobra para esquerda |
| **➡️ RIGHT / D** | Mover cobra para direita |
| **F11** | Alternar tela cheia |
| **BOOT SYSTEM** | Iniciar/pausar jogo |

---

### 🎯 Objetivo

```
┌─────────────────────────────────────────┐
│ CYBER-SNAKE.EXE — NEON OVERDRIVE       │
│                                         │
│ ENERGY: 150                             │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │ 🐍 🟩 🟩 🟩                      │   │
│  │        💎                        │   │
│  │    🟩 🟩 🟩 🟩 🟩 🟩            │   │
│  │                                 │   │
│  │                🟩 🟩 🟩 🟩 🟩    │   │
│  │                                 │   │
│  └─────────────────────────────────┘   │
│                                         │
│ [BOOT SYSTEM] [PAUSE SYSTEM]           │
└─────────────────────────────────────────┘
```

**Objetivo Principal**:
1. **Coma a comida** (💎 quadrado brilhante)
2. **Ganhe pontos** (cada alimento = 10 pontos)
3. **Cresça mais** (a cobra fica maior a cada refeição)
4. **Evite colisões** (com você mesma ou com as paredes)
5. **Atinja o máximo de pontos** antes de bater em si mesma

---

## 🎨 Modos de Dificuldade

### 🟢 **Estável (Fácil)**

```
Velocidade: 110ms por movimento
Ambiente: Verde escuro (#0a150a)
Cobra: Verde neon (#00FF41)
Comida: Branca (#FFFFFF)
Mechânica: Wrapping (passa pela borda)

ESTRATÉGIA:
✓ Perfeito para iniciantes
✓ Sem risco de bater na parede
✓ Tempo para pensar
✓ Ideal para aprender mecânicas
```

**Visuais**:
```
🟢 Cabeça verde brilhante
🟩 Corpo verde escuro
⬜ Alimento branco
🔲 Grid verde suave
```

---

### 🔵 **Beta (Médio)**

```
Velocidade: 85ms por movimento
Ambiente: Azul escuro (#0a0a15)
Cobra: Ciano neon (#00F2FF)
Comida: Rosa/Magenta (#FF0055)
Mechânica: Paredes = Game Over

DESAFIO:
⚡ Velocidade moderada
⚠️ Paredes são letais
🎯 Requer mais concentração
📈 Curva de aprendizado bem balanceada
```

**Visuais**:
```
🔵 Cabeça ciano brilhante
🟦 Corpo azul
🟩 Alimento magenta
```

---

### 🟠 **Sobrecarga (Difícil)**

```
Velocidade: 60ms por movimento
Ambiente: Vermelho escuro (#150a0a)
Cobra: Laranja neon (#FF9500)
Comida: Amarelo (#FFEE00)
Mechânica: Paredes são letais

HARDCORE:
⚡⚡ Muito rápido
🚨 Reação rápida necessária
💀 Um erro = Game Over
🏆 Para jogadores experientes
```

**Visuais**:
```
🟠 Cabeça laranja incandescente
🟧 Corpo laranja escuro
🟨 Alimento amarelo brilhante
```

---

### 🔴 **CRÍTICO (Expert)**

```
Velocidade: 40ms por movimento (25 FPS)
Ambiente: Vermelho sangue (#1a0000)
Cobra: Vermelho puro (#FF0000)
Comida: Magenta (#FF00FF)
Mechânica: Paredes são IMEDIATAS

IMPOSSÍVEL:
⚡⚡⚡ ABSURDAMENTE rápido
😱 Reflexos de profissional necessários
💀💀 Qualquer erro = FIM
🏅 Apenas para os melhores

⚠️ AVISO: Modo de bragging rights
```

**Visuais**:
```
🔴 Cabeça vermelha pura
🟥 Corpo vermelho escuro
🟣 Alimento magenta
```

---

## 🛠️ Tecnologias Utilizadas

| Componente | Tecnologia | Versão | Propósito |
|-----------|-----------|--------|----------|
| **Linguagem** | Python | 3.7+ | Lógica e estrutura |
| **GUI** | CustomTkinter | Latest | Interface moderna |
| **Canvas** | Tkinter | Nativo | Renderização 2D |
| **Random** | Nativo | Nativo | Posicionamento alimento |

---

## 🏗️ Arquitetura e Estrutura

### 📊 Fluxo do Jogo

```
┌──────────────────┐
│   CyberSnake     │
│   (Inicializa)   │
└────────┬─────────┘
         │
    ┌────▼─────────┐
    │ Seleciona    │
    │ Modo         │
    └────┬─────────┘
         │
    ┌────▼──────────────┐
    │ Pressiona BOOT    │
    │ SYSTEM            │
    └────┬──────────────┘
         │
    ┌────▼────────────────────────┐
    │ GAME LOOP                    │
    ├────────────────────────────┤
    │ 1. Lê input (setas/WASD)   │
    │ 2. Move cobra              │
    │ 3. Verifica colisões       │
    │ 4. Atualiza partículas     │
    │ 5. Renderiza tudo          │
    │ 6. Wait (modo speed)       │
    └────┬───────────────────────┘
         │
         ├─→ [Colisão?] ─→ GAME OVER
         │
         ├─→ [Comeu alimento?] ─→ Cresce + Score
         │
         └─→ [Ainda vivo?] ─→ LOOP
```

### 🧩 Componentes Principais

```
cobrinha.py
│
├── 📦 CLASSE: Particle (Efeitos visuais)
│   ├── __init__(canvas, x, y, color)
│   └── update() → bool
│
└── 🎮 CLASSE: CyberSnake (CustomTkinter)
    │
    ├── INICIALIZAÇÃO
    │   ├── __init__()
    │   ├── _setup_ui()
    │   ├─ _build_sidebar()
    │   └── _build_canvas()
    │
    ├── CONTROLES
    │   ├── _handle_input(event)
    │   ├── _change_dir(d)
    │   ├── _toggle_fullscreen()
    │   └── _toggle_game()
    │
    ├── CENÁRIOS/MODOS
    │   ├── _current_mode() → dict
    │   └── _update_scenario()
    │
    ├── LOOP PRINCIPAL
    │   └── _game_loop()
    │
    ├── LÓGICA DA COBRA
    │   ├── _move_snake(cfg)
    │   ├── _apply_bounds(hx, hy, cfg)
    │   ├── _collect_food()
    │   └── _spawn_food()
    │
    ├── PARTÍCULAS
    │   ├── _update_particles()
    │   └── _spawn_particles(x, y, color, count)
    │
    ├── RENDERIZAÇÃO
    │   ├── _render()
    │   ├── _draw_grid()
    │   ├── _draw_scanlines()
    │   ├── _draw_food(cfg)
    │   ├── _draw_snake(cfg)
    │   ├── _draw_head(sx, sy, cfg)
    │   └── _draw_segment(sx, sy, index, cfg)
    │
    └── GAME OVER
        ├── _game_over()
        └── _reset_state()
```

---

## 📚 Documentação das Principais Classes

### 1️⃣ `Particle` — Sistema de Efeitos

**Responsabilidade**: Partículas visuais que aparecem ao comer comida

```python
class Particle:
    """Partícula de efeito visual com vida e movimento próprio."""
    
    DECAY = 0.04  # Quanto a vida reduz por frame
    
    def __init__(self, canvas: tk.Canvas, x: float, y: float, color: str):
        """Cria partícula em posição (x, y) com cor."""
        self.canvas = canvas
        size = random.randint(1, 4)  # Tamanho aleatório 1-4px
        self.id = canvas.create_oval(x, y, x + size, y + size, 
                                    fill=color, outline="")
        self.vx = random.uniform(-5, 5)   # Velocidade X aleatória
        self.vy = random.uniform(-5, 5)   # Velocidade Y aleatória
        self.life = 1.0  # Vida 100% (desaparece quando ≤ 0)
    
    def update(self) -> bool:
        """Move partícula e reduz vida. Retorna False quando deve ser deletada."""
        self.canvas.move(self.id, self.vx, self.vy)  # Move
        self.life -= self.DECAY  # Envelhece
        if self.life <= 0:
            self.canvas.delete(self.id)  # Remove visualmente
            return False  # Sinal para remover da lista
        return True
```

**Fluxo**:
1. Partícula criada ao comer alimento
2. Se move aleatoriamente
3. Desaparece gradualmente
4. É removida quando vida ≤ 0

---

### 2️⃣ `CyberSnake` — Classe Principal

**Responsabilidade**: Gerenciar tudo (UI, lógica, renderização)

#### **Inicialização**

```python
def __init__(self):
    super().__init__()
    self.title("CYBER-SNAKE.EXE - NEON OVERDRIVE")
    self.geometry("1150x750")
    self.configure(fg_color="#000000")  # Preto absoluto
    
    # Estado do jogo
    self.snake = list(SNAKE_START)              # [(100,100), (80,100), (60,100)]
    self.direction = "Right"                    # Direção atual
    self.next_direction = "Right"               # Próxima direção
    self.food = (0, 0)                         # Posição alimento
    self.score = 0                             # Pontos
    self.running = False                       # Jogo rodando?
    self.particles: list[Particle] = []        # Efeitos visuais
    
    self.selected_mode = tk.StringVar(value="Beta (Médio)")
    
    self._setup_ui()
    self._update_scenario()
    self._spawn_food()
```

---

#### **Movimento da Cobra**

```python
def _move_snake(self, cfg: dict):
    """Move cobra, verifica colisões, come alimento."""
    # 1. ATUALIZAR DIREÇÃO
    self.direction = self.next_direction
    hx, hy = self.snake[0]  # Cabeça atual
    
    # 2. CALCULAR NOVA CABEÇA
    if   self.direction == "Up":    hy -= CELL      # (20px acima)
    elif self.direction == "Down":  hy += CELL      # (20px abaixo)
    elif self.direction == "Left":  hx -= CELL      # (20px esquerda)
    elif self.direction == "Right": hx += CELL      # (20px direita)
    
    # 3. APLICAR BORDAS
    hx, hy = self._apply_bounds(hx, hy, cfg)
    if hx is None:
        return  # Game over já chamado
    
    new_head = (hx, hy)
    
    # 4. VERIFICAR AUTO-COLISÃO
    if new_head in self.snake:
        self._game_over()
        return
    
    # 5. ADICIONAR CABEÇA
    self.snake.insert(0, new_head)
    
    # 6. VERIFICAR ALIMENTO
    if new_head == self.food:
        self._collect_food()  # Cresce
    else:
        self.snake.pop()  # Apenas se move
```

**Lógica**:
```
Cabeça: (100, 100)
Corpo:  [(80, 100), (60, 100)]
Move direita: Nova cabeça = (120, 100)
Insere: [(120, 100), (100, 100), (80, 100), (60, 100)]
Remove última: [(120, 100), (100, 100), (80, 100)] se não comeu
```

---

#### **Sistema de Bordas**

```python
def _apply_bounds(self, hx: int, hy: int, cfg: dict) -> tuple:
    """Wrapping (fácil) ou Game Over (outros modos)."""
    if cfg["wall_kill"]:  # Modo médio/difícil/expert
        if hx < 0 or hx >= CANVAS_W or hy < 0 or hy >= CANVAS_H:
            self._game_over()
            return None, None
    else:  # Modo fácil
        hx = hx % CANVAS_W   # Volta ao outro lado
        hy = hy % CANVAS_H
    return hx, hy
```

**Exemplos**:

```
MODO FÁCIL (wrapping):
x = -20 → x % 800 = 780 (volta ao lado direito)
x = 820 → x % 800 = 20 (volta ao lado esquerdo)

MODO MÉDIO/DIFÍCIL (wall_kill):
x = -20 → GAME OVER!
x = 820 → GAME OVER!
```

---

#### **Renderização**

```python
def _render(self):
    """Limpa canvas e redesenha tudo."""
    self.canvas.delete("game_obj")
    self.canvas.delete("grid")
    
    cfg = self._current_mode()
    
    self._draw_grid()          # Grid de fundo
    self._draw_scanlines()     # Efeito CRT
    self._draw_food(cfg)       # Alimento
    self._draw_snake(cfg)      # Cobra
```

**Ordem de Desenho** (de trás para frente):
1. Grid (fundo)
2. Scanlines (efeito retro)
3. Alimento (acima do fundo)
4. Cobra (acima de tudo)

---

#### **Desenho da Cobra**

```python
def _draw_head(self, sx: int, sy: int, cfg: dict):
    """Desenha cabeça com brilho externo."""
    # Brilho
    self.canvas.create_rectangle(
        sx - 2, sy - 2, sx + CELL + 2, sy + CELL + 2,
        outline=cfg["head"], width=1, tags="game_obj"
    )
    # Cabeça
    self.canvas.create_rectangle(
        sx, sy, sx + CELL, sy + CELL,
        fill=cfg["head"], outline="white", tags="game_obj"
    )

def _draw_segment(self, sx: int, sy: int, index: int, cfg: dict):
    """Desenha segmento com fade (decresce conforme distância)."""
    shrink = min(index, 8)  # Máx 8px de redução
    offset = shrink / 2
    self.canvas.create_rectangle(
        sx + offset, sy + offset,
        sx + CELL - offset, sy + CELL - offset,
        fill=cfg["tail"], outline=cfg["bg"], tags="game_obj"
    )
```

**Efeito Visual**:
```
Índice 0 (cabeça):  offset = 0, tamanho 20px (completo)
         1:         offset = 0.5, tamanho 19px
         2:         offset = 1, tamanho 18px
         ...
         8+:        offset = 4, tamanho 12px (mínimo)

Resultado: Cauda desaparece gradualmente! 🐍
```

---

## 📊 Exemplos de Gameplay

### Cenário 1: Começar no Modo Fácil

```
1. Abre programa
   → Snake no meio da tela
   → Alimento em lugar aleatório

2. Pressiona "BOOT SYSTEM"
   → Jogo inicia
   → Cobra começa a se mover

3. Digita SETAS para controlar
   ↑↑→→↓↓←← (formando quadrados)

4. Come alimento
   → Partículas aparecem
   → Score +10
   → Cobra cresce
   → Novo alimento spawna

5. Morre batendo em si mesma
   → "SYSTEM CRASH" aparece
   → Botão vira "REBOOT SYSTEM"
   → Pressiona para recomeçar
```

---

### Cenário 2: Desafio Expert

```
CRÍTICO (40ms = 25 FPS):

1. Pressiona START
   → Cobra VOANDO pela tela

2. Tenta usar SETAS
   → Input lag imperceptível
   → Reações humanas não acompanham

3. Primeira colisão
   → 3 segundos depois
   → GAME OVER

4. Score: 20 pontos
   → Frustrado, tenta novamente
```

---

## ⚙️ Mecânicas do Jogo

### 🍽️ Sistema de Comida

```python
def _spawn_food(self):
    """Posiciona alimento em célula aleatória (não ocupada)."""
    snake_set = set(self.snake)  # Converte para set (rápido)
    
    while True:  # Loop até encontrar posição válida
        x = random.randint(0, COLS - 1) * CELL    # Célula aleatória
        y = random.randint(0, ROWS - 1) * CELL
        
        if (x, y) not in snake_set:  # Se não ocupada
            self.food = (x, y)
            break
```

**Garantia**: Alimento sempre em célula vazia

---

### 🎨 Efeito Neon

```
Elementos visuais neon:
├─ Sidebar: #050505 (preto absoluto)
├─ Moldura: COLOR_ACCENT = "#00F2FF" (ciano)
├─ Canvas: [0a150a, 0a0a15, 150a0a, 1a0000]
├─ Grid: linhas tracejadas brancas
├─ Scanlines: linhas pretas (efeito CRT)
└─ Cores modo: Verde/Ciano/Laranja/Vermelho
```

**Resultado**: Aparência retro-futurista

---

### 🎯 Sistema de Pontos

```python
def _collect_food(self):
    """Aumenta score quando cobra come."""
    self.score += 10  # +10 pontos por alimento
    self.score_lbl.configure(text=f"ENERGY: {self.score}")
    self._spawn_food()
```

**Pontuação**:
- 🟨 1 alimento = 10 pontos
- 🟨 10 alimentos = 100 pontos
- 🟨 50 alimentos = 500 pontos

---

## 🚀 Como Rodar

### ✅ Pré-requisitos

- Python 3.7+
- pip

### 🔧 Passos

1. **Clone o repositório**:
```bash
git clone https://github.com/luisguigui/cobrinha-game.git
cd cobrinha-game
```

2. **Crie ambiente virtual**:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Instale dependências**:
```bash
pip install customtkinter
```

4. **Execute**:
```bash
python cobrinha.py
```

5. **Interface deve aparecer**:
   - Sidebar com modos
   - Canvas com grid
   - Pressione "BOOT SYSTEM" para começar

---

## 🎯 Estratégias de Jogo

### 🟢 **Modo Fácil** (Estável)

```
✅ Dicas:
1. Não se preocupe com velocidade
2. Pratique movimentos em grid
3. Aprenda padrões (quadrados, espirais)
4. Maximize pontos em modo "safe"

🎯 Meta: 500+ pontos
```

---

### 🔵 **Modo Médio** (Beta)

```
⚠️ Dicas:
1. Paredes são letais = foco constante
2. Não vire 180° (incorporado no código)
3. Planeje movimentos com antecedência
4. Evite "dead zones" (cantos)

🎯 Meta: 300+ pontos
```

---

### 🟠 **Modo Difícil** (Sobrecarga)

```
😰 Dicas:
1. Reflexos = tudo
2. Mantenha distância das paredes
3. Crie "corredor" de movimento
4. Pratique bastante antes

🎯 Meta: 200+ pontos
```

---

### 🔴 **Modo Expert** (CRÍTICO)

```
💀 Dicas:
1. Impossível para iniciantes
2. Apenas para desafio/diversão
3. Reflexos de jogador profissional
4. Uma morte é esperada

🎯 Meta: 100+ pontos (herói!)
```

---

## 🐛 Troubleshooting

### ❌ Problema: "ModuleNotFoundError: customtkinter"
**Solução**: `pip install customtkinter`

### ❌ Problema: Cobra não se move
**Causa**: Jogo não iniciado  
**Solução**: Pressione "BOOT SYSTEM"

### ❌ Problema: Controles não funcionam
**Causa**: Janela sem foco  
**Solução**: Clique na janela do jogo primeiro

### ❌ Problema: Velocidade muito alta/baixa
**Causa**: Modo diferente selecionado  
**Solução**: Escolha modo que prefere antes de iniciar

### ❌ Problema: Partículas não aparecem
**Causa**: Efeitos desabilitados ou performance  
**Solução**: Normal em modo "CRÍTICO" (prioriza FPS)

---

## ⚙️ Customização

### Alterar Velocidades

```python
MODES = {
    "Estável (Fácil)": {
        "speed": 110,  # ← Mude para 150 (mais lento)
        # ...
    },
}
```

### Alterar Cores

```python
MODES = {
    "Estável (Fácil)": {
        "head": "#00FF41",     # Verde
        "tail": "#005500",     # Verde escuro
        "food": "#FFFFFF",     # Branco
        # ...
    },
}
```

### Alterar Tamanho Canvas

```python
CANVAS_W = 800  # Mude para 1000
CANVAS_H = 600  # Mude para 800
```

### Alterar Tamanho da Célula

```python
CELL = 20  # Mude para 10 (mais células) ou 40 (menos)
```

---

## 💡 Dicas de Desenvolvimento

### Adicionar Novo Modo

```python
MODES = {
    # ... modos existentes ...
    "MÉGACRÍTICO": {
        "speed": 20,
        "bg": "#000000",
        "head": "#FF00FF",
        "tail": "#330033",
        "food": "#00FF00",
        "wall_kill": True,
    }
}
```

### Adicionar Sons

```python
# Import:
import winsound

# Ao comer:
def _collect_food(self):
    self.score += 10
    winsound.Beep(1000, 100)  # 1000Hz por 100ms
    # ...
```

---

## ✒️ Autores

**Luis Guilherme G.B.** & **Otávio César**

- 🐙 GitHub: [@luisguigui](https://github.com/luisguigui)
- 💼 Portfólio: Desenvolvedores Python
- 📧 Contato: Abra uma issue no repositório

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Use, modifique e distribua livremente!

---

## 🌟 Se gostou, considere dar uma ⭐!

```
   🐍 SNAKE NUNCA FOI TÃO NEON

   CYBER-SNAKE.EXE:
   Retro-futurismo em pixels

   ⭐ JOGUE, COMPETE, DIVIRTA-SE ⭐
```

---

**Última atualização**: 2026-04-20  
**Versão**: 1.0 — Neon Overdrive Edition  
**Status**: ✅ Production Ready  
**Foco**: Gameplay, Estética, Diversão
