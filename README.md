# Sigaa to Calendar <img src="https://lh3.googleusercontent.com/i4otanUG2PZ3BxLTg3oBCa0WDMMF2gMMQHg1EpyEhvbWtyrX2_kWCu2WynAxZxmgMPY" style="margin-bottom:-10px; border: solid white 2x">
### Organize seus horários do semestre rapidamente!

## O que é o Sigaa to Calendar?
 A ideia surgiu de uma necessidade real: tornar o processo de organização dos horários de cada matéria o mais simples e rápido possível.

Uma aplicação bastante utilizada com esse intuito é o Google Calendar (ou Google Agenda). No entanto, criar eventos manualmente e configura-los para atender cada uma das matérias pode se tornar uma tarefa repetitiva e um desperdício de tempo.

Com isso em mente, Sigaa to Calendar visa facilitar o processo de criação de eventos para todas as suas matérias de maneira completamente automática.

## Como funciona o Sigaa to Calendar?
A versão disponibilizada nesse repositório é um script em Python escrito de maneira didática de forma que seja fácil e transparente entender o que o programa faz a cada passo. Como não há uma API oficial que permita troca de informações com o SIGAA, o projeto implementa um web scraper que realiza o login e coleta da página principal somente as informações relevantes para a criação dos eventos (e nada mais). Em seguida, os eventos são formatados e passados para a API do Google Calendar para que sejam criados automaticamente em sua agenda.

## Instalação
<details>
<summary>Requisitos</summary>
    <ul>
    <li>Python 3.3 ou superior</li>
    </ul>
</details>

Clone esse repositório utilizando o comando:

```console
git clone https://github.com/melloirl/SigaaToCalendar
```
Ou faça o download do repositório em .zip clicando no botão "Code" acima.

Em seguida, acesse o diretório do projeto e execute o seguinte comando para instalar as bibliotecas necessárias:

```console
pip install -r requirements.txt
```
<details>
<summary>Ambiente Virtual</summary>
As bibliotecas necessárias podem ser instaladas globalmente, mas uma ideia interessante é utilizar um ambiente virtual. Essa abordagem pode evitar possíveis conflitos de versão com instalações prévias de pacotes.

Para criar um ambiente virtual, basta executar o comando:
```console
python -m venv .venv
```
E em seguida ativa-lo:

- Windows

```console
.venv\Scripts\activate.bat
```
- Linux

```console
$ source .venv/bin/activate
```

</details>

Para o funcionamento correto do programa é necessário criar um projeto no Google Cloud e habilitar a API do Google Calendar, gerando um token de credenciais.
O processo de obtenção do token é explicado mais detalhadamente <a href="https://developers.google.com/calendar/api/quickstart/python">aqui</a>.

## Utilização
Ao finalizar a instalação será necessário preencher o arquivo .env com as creendeciais de acesso do Sigaa.
 
<figure>
<img src="https://i.imgur.com/sWKe5WB.png">
<figcaption>O arquivo .env está localizado na pasta principal, mas também pode ser criado seguindo a estrutura acima.</figcaption>
</figure>

Finalmente, para adicionar seus cursos ao Google Calendar automaticamente basta executar o comando:

```console
python app.py
```
O andamento do script será mostrado no terminal juntamente de um link para visualizar os eventos criados.

<img src="https://i.imgur.com/rcD2B56.png">


## Transparência
Como mencionado acima, não há meio de comunicação oficial com a plataforma SIGAA até o presente momento. Por essa razão, para que os dados do aluno sejam obtidos é necessário que o usuário preencha as próprias informações através de um arquivo .env. Em momento algum esses dados são armazenados ou transmitidos a terceiros durante a execução do script. O código é aberto e exposto para que possam se verificar essas informações.

<div>
<img src="https://img.shields.io/github/issues/melloirl/SigaaToCalendar.svg">
<img src="https://img.shields.io/github/issues-pr/melloirl/SigaaToCalendar.svg">
<img src="https://img.shields.io/github/languages/code-size/melloirl/SigaaToCalendar">
<br>
<img src="http://ForTheBadge.com/images/badges/made-with-python.svg">
</div>
