from Booking import Booking
import datetime

with Booking() as bot:
  bot.pagina_inicial()
  bot.mudar_moeda("pt-br")
  bot.selecionar_local("Rio de janeiro")
  
  inicio = datetime.datetime(2022, 9, 20).strftime("%Y-%m-%d")
  termino = datetime.datetime(2022, 9, 23).strftime("%Y-%m-%d")

  bot.selecionar_datas(inicio, termino)
  bot.selecionar_quartos(2, 3)
 
 
 