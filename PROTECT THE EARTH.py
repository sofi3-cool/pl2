import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("xd" * count_heh)
    
@bot.command()
async def repit(ctx, wordrep, timecount):
    timecount = int(timecount)
    Totalword = " "
    for i in range(timecount):
        Totalword += wordrep + " "
    await ctx.send(Totalword) 
    
@bot.command()
async def suma(ctx, num1: int, num2: int):
    await ctx.send(num1 + num2)   
    
@bot.command()
async def tirar(ctx, sides: int):
    if sides < 6:
        await ctx.send("Por favor, ingresa un número de lados válido (mayor o igual a 6).")
        return  
    resultado = random.randint(1, sides)
    await ctx.send(resultado)  
       
     
@bot.command()
async def conversor(ctx, valor: float,  unit_1: str, unit_2: str):
    
    conversions = {
        # Distancias
        "km_millas": 0.621371,
        "millas_km": 1.60934,
        "m_ft": 3.28084,
        "ft_m": 0.3048,
        "cm_inch": 0.393701,
        "inch_cm": 2.54,

        # Pesos
        "kg_lbr": 2.20462,
        "lbr_kg": 0.453592,
        "gr_oz": 0.035274,
        "oz_gr": 28.3495,

        # Volúmenes
        "lt_gal": 0.264172,
        "gal_lt": 3.78541,
        "ml_tz": 0.00422675,
        "tz_ml": 236.588,
        "ml_lt": 0.001,
        "lt_ml": 1000,
    }

    # Temperturas
    if unit_1 == "c" and unit_2 == "f":
        result = (valor * 9 / 5) + 32
        await ctx.send(f"{valor} °C son {result} °F.")
    elif unit_1 == "f" and unit_2 == "c":
        result = (valor - 32) * 5 / 9
        await ctx.send(f"{valor} °F son {result} °C.")
    elif unit_1 == "c" and unit_2 == "k":
        result = valor + 273.15
        await ctx.send(f"{valor} °C son {result} K.")
    elif unit_1 == "k" and unit_2 == "c":
        result = valor - 273.15
        await ctx.send(f"{valor} K son {result} °C.")
    elif unit_1 == "f" and unit_2 == "k":
        result = (valor - 32) * 5 / 9 + 273.15
        await ctx.send(f"{valor} °F son {result} K.")
    elif unit_1 == "k" and unit_2 == "f":
        result = (valor - 273.15) * 9 / 5 + 32
        await ctx.send(f"{valor} K son {result} °F.")
    else:
        
        conversion_key = f"{unit_1}_{unit_2}"
        if conversion_key in conversions:
            factor = conversions[conversion_key]
            result = valor * factor
            await ctx.send(f"{valor} {unit_1} son {result} {unit_2}.")
        else:
            await ctx.send(f"No se puede convertir de {unit_1} a {unit_2}. Unidades no compatibles.")
            
            
@bot.command()
async def img1(ctx):
    with open('Botclass/img/img1.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    
@bot.command()
async def img2(ctx):
    with open('Botclass/img/img2.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    
@bot.command()
async def img3(ctx):
    with open('Botclass/img/img3.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)        
    
       
                            
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)  
    
    
def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def dog(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)   
    
    
@bot.command()
async def math(ctx):
    list_img = os .listdir('Botclass/mathmem')
    ruta = f'Botclass/mathmem/{random.choice(list_img)}'
    with open(ruta, 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    
    
@bot.command()
async def event(ctx):
    fecha = [
        "2024-12-05", 
        "2024-12-07", 
        "2024-12-10", 
        "2024-12-12", 
        "2024-12-14"
        ]
    
    hora = [
        "09:00", 
        "11:30", 
        "14:00", 
        "16:00", 
        "10:30"
        ]
    
    sitio = [
        "Parque Nacional Natural Tayrona", 
        "Ciudad Perdida Teyuna", 
        "Playa Blanca, Barú", 
        "Auditorio Municipal", 
        "Parque Espiritu del Manglar"
        ]
    
    tematica = [
        "Reciclaje y reducción de residuos plásticos",
        "Acción comunitaria contra la contaminación del aire",
        "Protección de los ecosistemas marinos y reducción del uso de plásticos",
        "Conservación de recursos naturales y energías renovables",
        "Restauración de áreas verdes y prevención de la deforestación"
        ]
    
    fechas = random.choice(fecha)
    horas = random.choice(hora)
    sitios = random.choice(sitio)
    tematicas = random.choice(tematica)
    

    
    if sitios == "Parque Nacional Natural Tayrona":
        imagen = "tayrona.jpg"
    elif sitios == "Ciudad Perdida Teyuna":
        imagen = "teyuna.jpg"
    elif sitios == "Playa Blanca, Barú":
        imagen = "baru.jpg"
    elif sitios == "Auditorio Municipal":
        imagen = "auditorio.png"
    elif sitios == "Parque Espiritu del Manglar":
        imagen = "manglar.jpg" 
    else:
        imagen = "pordefecto.jpg"    
        
    
    mensaje = f"""   
    Evento: {tematicas}
    Fecha: {fechas}
    Hora: {horas}
    Sitio: {sitios}
    """
  
    ruta = f"Botclass/contaminacion/{imagen}"
    with open (ruta, "rb") as f:
        picture = discord.File(f)
    await ctx.send(mensaje, file=picture)
bot.run("TU PIN DE DISCORD VA AQUí")      
