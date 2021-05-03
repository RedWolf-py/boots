from selenium.webdriver import Firefox   #pode substituir pelo Chrome
import time
import random


driver = Firefox()  #pode substituir pelo Chrome
driver.get('https://www.instagram.com/')

def loguin_page(firefox, loguin, senha, amigos):

	time.sleep(4)
	driver.find_element_by_name('username').send_keys(loguin)
	driver.find_element_by_name('password').send_keys(senha)
	time.sleep(2)
	driver.find_element_by_css_selector('[type="submit"]').click()
	time.sleep(5)
	driver.find_element_by_css_selector('[autocapitalize="none"]').send_keys(amigos)
	time.sleep(5)
	driver.find_element_by_css_selector('[role="none"]').click()

                #seu usuario ,sua senha,  amigo que voce vai curti,comentar as fotos ou hastag
loguin_page(driver, 'snoop', '123456789', 'chihuahua')

# coloca os cometarios, que voce quer por, na pagina do seu amigo,pode apagar e subtituir estes
comentarios = ["muito linda(o)", "que fofo!","me segue amigo,se ainda nao esta seguindo", "amei !!!","me segue aumigo", "au au kkkkkk", "adoravel", "da uma olhada no meu album amigo", "visitinha diaria amigo", "amei seu album", "lindas fotos", "Que amor", "vcs são anjos disfarçados", "gostei demais", "beautiful pics", "anjos de quatro patas","que belo"]

for i in range(1, 5):

	driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
	time.sleep(3)

def curt_foto():

	for i in range(1, 2):
		
		curti = driver.find_element_by_css_selector('[aria-label="Curtir"]')
		curti.click()

def digitar_como_humano(frase, teclado):

	for escrevendo in frase:
		teclado.send_keys(escrevendo)
		time.sleep(random.randint(10,20)/120)

tagis = driver.find_elements_by_tag_name('a')

expandir = []

foto_abrir = [elem.get_attribute("href") for elem in tagis]
print(foto_abrir)

print(f'fotos:',str(len(foto_abrir)))


for link in foto_abrir:
    try:
        if link.index("/p/") != -1:
            expandir.append(link)

    except:
        pass

print(expandir)


for expandir in expandir:

	loopp = driver.get(expandir)
	driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
	time.sleep(6)

	curt_foto()

	time.sleep(2)
	enviar = driver.find_element_by_class_name('Ypffh').click()
	comentar = driver.find_element_by_class_name('Ypffh')
	time.sleep(5)
	digitar_como_humano(random.choice(comentarios), comentar)
	time.sleep(8)
	final = driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()

driver.close()



#By Alê