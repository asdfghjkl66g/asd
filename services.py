services:
  - type: web
    name: my-telegram-bot
    runtime: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "python bot.py"
    region: frankfurt
    plan: free