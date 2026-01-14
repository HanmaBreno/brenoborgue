import discord # DEPENDENCIAS
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# 🔹 CANAIS
CANAIS_PERMITIDOS = {
    1350887176518238401, 1458287385937969185
}

# 🔹 CHANCE (30%)
CHANCE_RESPONDER = 30  # porcentagem

# 🔹 MENSAGENS BISONHAS
RESPOSTAS = {
    #DAVI
    315549004274597888: [
        "Cala a boca Daviacaboom 😡",
        "Tu quer oq aonde? 🥵",
        "Lá vem ele querendo falar alemão denovo 🙄",
        "Nossa Davi... Nossa Davi",
        "Te odeio",
        "Morre daviacaboom",
        "Chamaram o especialista em nada?",
        "Quer atenção?",
        "Todo dia isso, Davi?",
        "Ninguém chamou, mas ele veio",
        "Arquivo .ex aberto novamente",
        "Já voltou pra ex hoje ou só mais tarde?",
        "Revivendo DLC antiga",
        "Opa como ta a dignissima (ex)",
        "Já falou de ex hoje? rs",
        "Aparané",
        "Calma amor",
        "Olá, Davia A. Quem não chora não mama",
    ],
    #lUCAS
    1414038933494567024: [
        "Cala a boca Luquete 😡",
        "Chegou o fura balão 🙄",
        "Lá vem o caçador de pokémon suspeito 🥵",
        "Cala boca viadinho",
        "Tu quer leitinho?",
        "Apaga que ainda dá tempo",
        "O coisa ruim chegou",
        "Alguém esconde os balões",
        "Calma macaco dardo (essa é só pra quem jogou bloons TD6 as 19:30 na segunda-feira)",
        "Luquete detectado, balões em risco",
        "Nerd fudido",
        "Tá bom ou não tá ruim?",
        "blibliblibli",
        "Pq não bombom?",
    ],
    # JAO
    416041382965411840: [
        "Oi Jão 😣",
        "Tchau Jão",
        "Fala direito Jão",
        "Taquientaouai",
        "Elsa",
        "Calma Jão",
        "De novo isso Jão?",
        "Não Jão… não",
        "Tá bom Jão",
        "Silêncio Jão",
        "Me come Jão 🤤",

    ],
    # BRENO
    389029214847893505: [
        "Chegou o protagonista",
        "Todo mundo sabe que a cópia é melhor que você né",
        "Cala a boca lixo 🤬",
        "Ja mandei calar a boca né",
        "Tomar no seu cu",
        "Brenoborgue > breno lixo",
        "Volta pro modo silencioso, por favor",
        "Calma BrenBren",
        "Cansou de ficar com ela?",
        "Ain eu to estudando - disse a putinha",
        "O fodão chegou",
        "Oi papai",
        "Chegou o goza e dorme",
    ],
    # BLENINN
    505935179928567818: [
        "Fala engole garota",
        "Chegou o vacilão",
        "Cala a boca cabeça de satélite",
        "Isso que dá me trocar por ela",
        "Morre Breno",
        "Cabaçei",
        "Vacilão",
    ]
    
}

@bot.event # STATUS
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # 
    if message.channel.id not in CANAIS_PERMITIDOS:
        return

    user_id = message.author.id

    # 
    if user_id not in RESPOSTAS:
        return

    # 
    sorteio = random.randint(1, 100)
    if sorteio > CHANCE_RESPONDER:
        return  # Não responde

    # 
    resposta = random.choice(RESPOSTAS[user_id])
    await message.reply(resposta)

    await bot.process_commands(message)

# TOKEN
import os

bot.run(os.getenv("TOKEN"))


