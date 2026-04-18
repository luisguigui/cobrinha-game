🐍 CYBER-SNAKE.EXE — NEON OVERDRIVE
CYBER-SNAKE é uma reinterpretação moderna e estilizada do clássico "Jogo da Cobrinha". Desenvolvido com uma interface futurista baseada em CustomTkinter, o jogo apresenta efeitos de partículas, múltiplas dificuldades e uma atmosfera visual inspirada na estética Cyberpunk.

🚀 Funcionalidades
Interface Neon: Design moderno com paleta de cores vibrantes e efeitos de scanlines no canvas.

Dificuldades Dinâmicas: 4 modos de jogo que alteram velocidade, cores e comportamento das bordas:

🟢 Estável (Fácil): Velocidade reduzida e sem colisão com paredes.

🔵 Beta (Médio): Velocidade equilibrada e paredes fatais.

🟠 Sobrecarga (Difícil): Movimentação rápida e alto contraste.

🔴 CRÍTICO (Expert): Velocidade máxima para reflexos sobre-humanos.

Sistema de Partículas: Efeitos visuais dinâmicos durante o loop do jogo.

Modo Fullscreen: Suporte à imersão total via tecla F11.

Controles Híbridos: Jogue usando as setas do teclado ou as teclas WASD.

🛠️ Tecnologias Utilizadas
O projeto foi construído utilizando:

Python (Lógica principal)

CustomTkinter (Interface de usuário moderna)

Tkinter (Renderização de Canvas e Back-end da interface)

📋 Pré-requisitos
Antes de executar o sistema, você precisará instalar a biblioteca customtkinter:

Bash
pip install customtkinter
🎮 Como Jogar
Execução:

Bash
python cyber_snake.py
Comandos:

W / ⬆️: Mover para Cima

S / ⬇️: Mover para Baixo

A / ⬅️: Mover para Esquerda

D / ➡️: Mover para Direita

F11: Alternar Tela Cheia

Objetivo: Colete os núcleos de energia (comida) para aumentar sua pontuação (ENERGY) sem colidir com o próprio corpo ou com as bordas (nos modos avançados).

🏗️ Estrutura do Código
Particle: Classe responsável pelos efeitos visuais de movimento e "fade" no cenário.

CyberSnake: Classe principal que gerencia o loop do jogo, detecção de colisões e atualização da UI.

MODES: Dicionário de configuração que mapeia as constantes de dificuldade.

👥 Desenvolvedores
Projeto criado por:

Luis Guilherme G.B.

Otavio Cesar

Aviso de Sistema: Se a cobra colidir, o sistema entrará em estado de SYSTEM CRASH. Reinicie o hardware através do botão REBOOT SYSTEM.
