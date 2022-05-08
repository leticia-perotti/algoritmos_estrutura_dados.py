import re
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.utils import get_color_from_hex as C
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from random import choice
import lista

Window.clearcolor = 1,1,1,1
palavras = lista.aleatorias

kvcode = """
#: import C kivy.utils.get_color_from_hex
#: import FadeTransition kivy.uix.screenmanager.FadeTransition
<MyButton@Button>:
	font_size: "20sp"
	size_hint: (.100, .065)
	background_normal: ""
    color: C("#000000")
	background_color: C("#FFFFFF")
	
ScreenManager:
	id: scr_manager	
	Inicio:
		name: 'inicio'
	Jogo:
		name: 'jogo'
<Inicio>:
	
	BoxLayout:
		
		Button:
			text:"Bem vindo ao jogo da forca, click para começar"
			on_press: root.jogar()
		
<Jogo>:
	on_enter: root.sortear_palavra()
	BoxLayout:
		orientation: 'vertical'
			
		Image:
			id: image
			source: "image/1.jpg"
			
		Label:
			text: root.lbl_tentativas
			halign: "center"
			valign: "middle"
			color: C("B22222")
			font_size: "25sp"
			size_hint: (1, .15)
			markup: True
		
		Label:
			text: root.lbl_certas
			halign: "center"
			valign: "middle"
			color: C("1E90FF")
			font_size: "40sp"
			size_hint: (1,.2)
			markup: True
          
        MyButton:
			text: "A"
            id: letra
            value: 'A'
			on_release:  root.chute('A')
            
            pos_hint: {'x' : .1, 'y' : .1}

        MyButton:
			text: "B"
            id: letra
            value: 'B'
			on_release: root.chute('B')
            pos_hint: {'x' : .2, 'y' : .1}

        MyButton:
			text: "C"
            id: letra
            value: 'C'
			on_release: root.chute('C')
            pos_hint: {'x' : .3, 'y' : .1}

        MyButton:
			text: "D"
            id: letra
            value: 'D'
			on_release: root.chute('D')
            pos_hint: {'x' : .4, 'y' : .1}
        
        MyButton:
			text: "E"
            id: letra
            value: 'E'
			on_release: root.chute('E')
            pos_hint: {'x' : .5, 'y' : .1}

        MyButton:
			text: "F"
            id: letra
            value: 'F'
			on_release: root.chute('F')
            pos_hint: {'x' : .6, 'y' : .1}

        MyButton:
			text: "G"
            id: letra
            value: 'G'
			on_release: root.chute('G')
            pos_hint: {'x' : .7, 'y' : .1}

        MyButton:
			text: "H"
            id: letra
            value: 'H'
			on_release: root.chute('H')
            pos_hint: {'x' : .8, 'y' : .1}

        MyButton:
			text: "I"
            id: letra
            value: 'I'
			on_release: root.chute('I')
            pos_hint: {'x' : .1, 'y' : .2}
        
        MyButton:
			text: "J"
            id: letra
            value: 'J'
			on_release: root.chute('J')
            pos_hint: {'x' : .2, 'y' : .2}
        
        MyButton:
			text: "K"
            id: letra
            value: 'K'
			on_release: root.chute('K')
            pos_hint: {'x' : .3, 'y' : .2}
        
        MyButton:
			text: "L"
            id: letra
            value: 'L'
			on_release: root.chute('L')
            pos_hint: {'x' : .4, 'y' : .2}
        
        MyButton:
			text: "M"
            id: letra
            value: 'M'
			on_release: root.chute('M')
            pos_hint: {'x' : .5, 'y' : .2}
        
        MyButton:
			text: "N"
            id: letra
            value: 'N'
			on_release: root.chute('N')
            pos_hint: {'x' : .6, 'y' : .2}
        
        MyButton:
			text: "O"
            id: letra
            value: 'O'
			on_release: root.chute('O')
            pos_hint: {'x' : .7, 'y' : .2}
        
        MyButton:
			text: "P"
            id: letra
            value: 'P'
			on_release: root.chute('P')
            pos_hint: {'x' : .8, 'y' : .2}
        
        MyButton:
			text: "Q"
            id: letra
            value: 'Q'
			on_release: root.chute('Q')
            pos_hint: {'x' : .1, 'y' : .3}

        MyButton:
			text: "R"
            id: letra
            value: 'R'
			on_release: root.chute('R')
            pos_hint: {'x' : .2, 'y' : .3}

        MyButton:
			text: "S"
            id: letra
            value: 'S'
			on_release: root.chute('S')
            pos_hint: {'x' : .3, 'y' : .3}

        MyButton:
			text: "T"
            id: letra
            value: 'T'
			on_release: root.chute('T')
            pos_hint: {'x' : .4, 'y' : .3}
        
        MyButton:
			text: "U"
            id: letra
            value: 'U'
			on_release: root.chute('U')
            pos_hint: {'x' : .5, 'y' : .3}

        MyButton:
			text: "V"
            id: letra
            value: 'V'
			on_release: root.chute('V')
            pos_hint: {'x' : .6, 'y' : .3}

        MyButton:
			text: "W"
            id: letra
            value: 'W'
			on_release: root.chute('W')
            pos_hint: {'x' : .7, 'y' : .3}

        MyButton:
			text: "X"
            id: letra
            value: 'X'
			on_release: root.chute('X') 
            pos_hint: {'x' : .8, 'y' : .3}           

        MyButton:
			text: "Y"
            id: letra
            value: 'Y'
			on_release: root.chute('Y') 
            pos_hint: {'x' : .1, 'y' : .4}           

        MyButton:
			text: "Z"
            id: letra
            value: 'Z'
			on_release: root.chute('Z')
            pos_hint: {'x' : .2, 'y' : .4}            
           			
		Label:
			size_hint: (.5, .07)
"""

# tela de inicio com o botãozinho
class Inicio(Screen):
	def jogar(self):

		self.manager.current = "jogo"
		certas = ''
		self.manager.get_screen('jogo').lbl_certas = str((','.join(certas)).replace(',',' '))

# tela do jogo
class Jogo(Screen):

	lbl_certas = StringProperty('')
	lbl_tentativas = StringProperty('Tentativas:')

	def __init__(self, *args, **kwargs):
		super(Jogo, self).__init__(*args, **kwargs)
    
	def sortear_palavra(self):
		global palavra, certas, erros, sorteio, contador

		erros = ['Erros:\n']
		contador = 0
		self.ids.image.source = "image/1.jpg"
		
		sorteio = choice(palavras).upper()
		palavra = sorteio

		certas = ['_' for x in palavra]
		self.atualizar_label()

	def chute(self, chuteLetra):
		chute = chuteLetra.upper()

		if chute != "":
			for letra in range(0, len(palavra)):
				if chute == palavra[letra]:
					certas[letra] = chute

			for letra in range(0, len(palavra)):
				if chute != palavra[letra]:
					if chute not in certas:
						if chute not in erros:
							erros.append(chute)
							self.trocar_imagem()

			self.atualizar_label()

	def atualizar_label(self):
		global contador
		if contador <= 6:
			self.lbl_certas = str((','.join(certas)).replace(',',' '))
			self.lbl_tentativas = str((','.join(erros)).replace(',', ' '))

			if "_" not in certas:
				self.ids.image.source = "image/1.jpg"
				self.lbl_certas = '[color=008000]%s[/color]'%(sorteio)
				self.lbl_tentativas = '[color=008000]Você acertou![/color]'
				
	def trocar_imagem(self):
		imagens = [
			"image/2.jpg", "image/3.jpg", "image/4.jpg",
			"image/5.jpg", "image/6.jpg", "image/7.jpg", 
			"image/8.jpg"
		]
		global contador
		
		if contador == 6:
			self.ids.image.source = imagens[contador]
			self.lbl_certas = '[color=B22222]%s[/color]'%(sorteio)
			self.lbl_tentativas = '[color=B22222]Você perdeu![/color]'
		elif contador <= 6:
			self.ids.image.source = imagens[contador]
            
		contador += 1

	def sair(self):
		App.get_running_app().stop()

      
class ForcaApp(App):

	def build(self):
		main_widget = Builder.load_string(kvcode)
		return main_widget

if __name__ == '__main__':
	ForcaApp().run()