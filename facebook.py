# coding:utf-8
# by ins3c7, feb., 2016

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from gtk import gdk
import time, os, random, sys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from subprocess import Popen, PIPE

class CygwinFirefoxProfile(FirefoxProfile):

	@property
	def path(self):

		path = self.profile_dir

		# cygwin requires to manually specify Firefox path a below:
		# PATH=/cygdrive/c/Program\ Files\ \(x86\)/Mozilla\ Firefox/:$PATH
		try:
			proc = Popen(['cygpath','-d',path], stdout=PIPE, stderr=PIPE)
			stdout, stderr = proc.communicate()
			path = stdout.split('\n', 1)[0]

		except OSError:
			print("No cygwin path found")

		return path

class facebook:
	os.system('clear')

	print '[#] Carregando, aguarde...\n'

	bro = ''

	tempoadd = 4
	intervalo = 0.03
	segundosmax = 3
	intervalo_adicionar = [4.9, 3.6, 2.5, 6.2, 10.3, 7.5, 8.8]

	solicitacoes = 30

	tela_w = ((gdk.screen_width() / 2) + 30)
	tela_h = (gdk.screen_height() - 60)

	pagina = 'https://www.facebook.com/pravocemamae'
	
	conta = ''
	logado = False

	proxys = [
				'189.113.135.230:8080', # boa
				'177.44.196.254:3128', # media
				'201.48.251.229:3128', # boa
				'187.49.112.38:8080', # boa
				'187.108.190.215:3128', # boa
				'201.48.251.236:3128', # boa
				'186.229.16.154:80', # broken
				'150.161.21.242:8080', # slow
				'189.8.195.2:80', # boa
				'200.237.249.55:80',
				'177.69.61.114:80', # slow
				'200.192.252.130:8080', # medium
				'177.91.23.221:8080', # slow

			]

	def logar(self):
		os.system('clear')
		print '[#] Carregando, aguarde....'

		firefoxProfile = CygwinFirefoxProfile()
		firefoxProfile.set_preference('permissions.default.image', 2)

		self.bro = webdriver.Firefox(firefoxProfile)
		self.bro.get('https://www.facebook.com/')
		os.system('clear')

		emails = [
					'deniserocha@mohmal.com|********',
					'camilaroberta33@mohmal.com|********',
					'prisciladiascampos@mohmal.com|********',
					'carolbiancacastilho@mohmal.com|********',
					'carolbeatrizcosta@mohmal.com|********',
					'carolborges@mohmal.com|********',
					'talitacampos@mohmal.com|********',
					'isabelalopesdias@mohmal.com|********', # 138.36.27.5:3128
					'anaisabela@mohmal.com|********',
					'gabidias56@mohmal.com|********',
					'analuiza56@mohmal.com|********',
					'samantarios65@mohmal.com|********',
					'carolinadiasfonseca@mohmal.com|********',
					'carolrocha91@mohmal.com|********',

				]

		print '[#] Escolha a conta:\n'
		x = 1
		for mails in emails:
			print '[/]', str(x)+'.', mails.split('@')[0], '-', str(mails.split('@')[1].split('.')[0]).upper()
			x += 1

		print '\n[/] 0. Voltar'

		email = raw_input('\n[..] Digite o número:\033[33m ')
		print '\033[0;0m'

		if int(email) == 0:
			self.logado = False
			self.bro.close()
			return

		conta_email, senha_email =  emails[int(email) - 1].split('|')
		self.conta = conta_email
		email = self.bro.find_element_by_xpath("//input[@name='email']")
		email.send_keys(conta_email)

		senha = self.bro.find_element_by_xpath("//input[@name='pass']")
		senha.send_keys(senha_email)

		try:
			login = self.bro.find_element_by_xpath("//label[@id='loginbutton']")
			login.send_keys(Keys.RETURN)
		except:
			raw_input('[!] Clique em LOGAR. Depois pressione ENTER.')
			pass

		self.logado = True

	def adicionar(self):
		self.bro.get('https://www.facebook.com/find-friends/browser/')
		elm = self.bro.find_elements(By.XPATH, '//button[text()="Adicionar aos amigos"]')
		len_elm = len(elm)
		calc_convites = 'Menos de 10' if int(len_elm) < 10 else str(len_elm)
		print '\n[$]', calc_convites, 'convites foram carregados. Iniciando...'
		print '[$] Adicionando amigos...'
		random.shuffle(elm)
		for e in elm:
			try:
				e.send_keys(Keys.RETURN)
				time.sleep(random.choice(self.intervalo_adicionar))
			except:
				pass

		elm = ''
		raw_input('\n[!] Pressione ENTER para continuar.\n')

	def confirmar(self):
		qtd = 0
		while 1:
			self.bro.get('https://www.facebook.com/friends/requests/?fcref=jwl')
			print '\n[$] Procurando solicitações. Aguarde...'
			elm = self.bro.find_elements(By.XPATH, '//button[text()="Confirmar"]')
			len_elm = len(elm);random.shuffle(elm);
			if len_elm < 1:break
			calc_convites = 'Menos de 10' if int(len_elm) < 10 else str(len_elm)
			print '\n[$]', calc_convites, 'convites foram carregados. Iniciando...'
			qtd += len_elm
			adicionou = 0
			if (len(elm)) < 20:
				break
			i = 1
			for e in elm:
				print '\r'+'\033[41m[%%] Adicionando %d de %d \33[0;0m' % (i, len_elm),
				sys.stdout.flush()
				i += 1
				try:
					adicionou += 1
					e.send_keys(Keys.RETURN)
					time.sleep(random.choice(self.intervalo))
				except:
					pass
			adds = int(adicionou)
			print '\033[30m'+'[+] COMPLETO! {} solicitações confirmadas.\033[0;0m'.format(str(adds))
		print '\n[#] Total de {} convites confirmados.'.format(str(qtd))
		elm = ''
		raw_input('\n[!] Pressione ENTER para continuar.\n')

	def convidar(self):
		try:
			print '\n[#] Iniciando, aguarde...'
			self.bro.get(self.pagina)
			frst = self.bro.find_element_by_partial_link_text('Convidar amigos')
			frst.send_keys(Keys.RETURN)
			raw_input('[!] Faça o primeiro convite manualmente.. Depois pressione Enter!')
			elm = self.bro.find_elements_by_link_text('Convidar')
			len_elm = len(elm);random.shuffle(elm)
			calc_convites = 'Menos de 10' if int(len_elm) < 10 else str(len_elm)
			print '\n[$]', calc_convites, 'convites foram carregados. Iniciando...'
			# self.bro.set_window_size(700, 200)
			i = 1
			for e in elm:
				print '\r'+'\033[41m[%%] Adicionando %d de %d \33[0;0m' % (i, len_elm),
				sys.stdout.flush()
				i += 1
				try:
					e.send_keys(Keys.RETURN)
					time.sleep(random.choice(self.intervalo))
				except:
					pass
			elm = ''
		except Exception, e:
			print str(e)

		raw_input('\n[!] Pressione ENTER para continuar.\n')

	def curtir(self):
		elm = self.bro.find_elements_by_link_text('Curtir')
		len_elm = len(elm);random.shuffle(elm);
		print '\n[$]', str(len(elm)), 'curtidas foram carregadas. Iniciando...'
		print '\n[$] Enviando curtidas...'
		for e in elm:
			print '\r'+'\033[41m[%%] Adicionando %d de %d \33[0;0m' % (i, len_elm),
			sys.stdout.flush()
			i += 1
			try:
				e.send_keys(Keys.RETURN)
				time.sleep(random.choice(self.intervalo))
			except:
				pass
		elm = ''
		raw_input('\n[!] Pressione ENTER para continuar.\n')

	def cadastrar(self):
		# os.system('clear')
		print '[#] Escolha da proxy:\n'
		print '[/] 1. Sortear proxy'
		print '[/] 2. Digitar proxy\n'

		opcao = raw_input('[..] Escolha uma opção: ')

		if int(opcao) == 1:
			_proxy = random.choice(self.proxys)
		else:
			# os.system('clear')
			_proxy = raw_input('[..] Digite a proxy: ')

		_proxy = str(_proxy)

		# os.system('clear')

		emails = [
			'',
		]

		try:
			# print '[#] Escolha a conta:\n'
			# x = 1
			# for mails in emails:
			# 	print '[/]', str(x)+'.', mails.split('@')[0], '-', str(mails.split('@')[1].split('.')[0]).upper()
			# 	x += 1

			# print '[/] 0. Voltar\n'
			print '\033[30m'+'[^] Proxy:', str(_proxy) + '\033[0;0m\n'

			# email = raw_input('\n[..] Digite o número:\033[33m ')
			# print '\033[0;0m'

			# if int(email) == 0:
			# 	self.bro.close()
			# 	return

			# login, senha =  emails[int(email) - 1].split('|')
			self.conta = 'TESTE@TESTE'

			webdriver.DesiredCapabilities.FIREFOX['proxy']={
				"httpProxy":_proxy,
				"ftpProxy":_proxy,
				"sslProxy":_proxy,
				"noProxy":None,
				"proxyType":"MANUAL",
				"autodetect":False
			}


			firefoxProfile = CygwinFirefoxProfile()
			firefoxProfile.set_preference('permissions.default.image', 2)
			self.bro = webdriver.Firefox(firefoxProfile)

			self.bro = webdriver.Firefox()
			self.bro.set_page_load_timeout(80)
			self.bro.set_window_size(self.tela_w, self.tela_h)
			self.bro.set_window_position(850, 0)
			self.bro.get('https://www.facebook.com/')

			# if 'Log' not in self.bro.title:
			# 	print '[!] Proxy não funcionou. Reiniciando...'
			# 	# self.proxys.remove(_proxy)
			# 	_proxy = random.choice(self.proxys)
			# 	self.bro.close()
			# 	pass

			# try:
			# 	_login = self.bro.find_element_by_xpath("//input[@name='email']")
			# 	_login.send_keys(login)

			# 	_senha = self.bro.find_element_by_xpath("//input[@name='pass']")
			# 	_senha.send_keys(senha)

			# 	try:
			# 		logins = self.bro.find_element_by_xpath("//label[@id='loginbutton']")
			# 		logins.send_keys(Keys.RETURN)

			# 	except Exception, e:
			# 		print '[-] ERRO 4:', str(e)
			# 		# raw_input('[!] Clique em LOGAR depois pressione ENTER.\n')
			# 		pass

			# except Exception, e:
			# 	print '[-] ERRO 3:', str(e)
			# 	# raw_input('[!] Pressione ENTER.\n')
			# 	pass

			# if 'Entrar' in self.bro.title or 'Log' in self.bro.title:
			# 	pass

		except Exception, e:
			print '[ERRO]', str(e)

		self.logado = True
		elm = ''
		raw_input('Pressione ENTER para continuar.')


	def checar_login(self):
		try:
			emails = []
			# mails = open('emails/hotmail.txt', 'r').readlines()
			mails = open('logins.txt', 'r').readlines()

			for line in mails:
				if len(line):
					emails.append(line.rstrip().split())

			_proxy = random.choice(self.proxys)

			# random.shuffle(emails)

			for mail in emails:

				try:
					if len(mail):
						login, senha = mail
						os.system('clear')

						webdriver.DesiredCapabilities.FIREFOX['proxy']={
							"httpProxy":_proxy,
							"ftpProxy":_proxy,
							"sslProxy":_proxy,
							"noProxy":None,
							"proxyType":"MANUAL",
							"autodetect":False
						}

						print
						print '[#] Testando login...\n'
						print '[^] Proxy:', _proxy
						print '[@] Email:', login
						print '[*] Senha:', senha
						print

						if self.bro:
							self.bro.close()
						self.bro = webdriver.Firefox()
						self.bro.set_page_load_timeout(40)
						# self.bro.implicitly_wait(10)
						self.bro.set_window_size(self.tela_w, self.tela_h)
						self.bro.set_window_position(850, 0)
						self.bro.get('https://www.facebook.com/')

						if 'Log' not in self.bro.title:
							print '[!] Proxy não funcionou. Reiniciando...'
							# self.proxys.remove(_proxy)
							_proxy = random.choice(self.proxys)
							self.bro.close()
							pass

						try:
							_login = self.bro.find_element_by_xpath("//input[@name='email']")
							_login.send_keys(login)

							_senha = self.bro.find_element_by_xpath("//input[@name='pass']")
							_senha.send_keys(senha)

							try:
								logins = self.bro.find_element_by_xpath("//label[@id='loginbutton']")
								logins.send_keys(Keys.RETURN)

							except Exception, e:
								print '[-] ERRO 4:', str(e)
								raw_input('[!] Clique em LOGAR depois pressione ENTER.\n')
								pass

						except Exception, e:
							print '[-] ERRO 3:', str(e)
							raw_input('[!] Pressione ENTER.\n')
							pass

						if 'Entrar' in self.bro.title or 'Log' in self.bro.title:
							pass

						else:
							self.logado = True
							logins = open('logins.txt', 'a')
							logins.write('{}:{}|{}\r\n'.format(login, senha, _proxy))
							logins.close()
							self.bro.set_window_size(self.tela_w, self.tela_h)
							self.convidar()
							pass

						self.bro.close()

 						os.system('clear')

				except KeyboardInterrupt:
					self.bro.close()
					return

				except Exception, e:
					print '[-] ERRO 2:', str(e)
					_proxy = random.choice(self.proxys)
					pass

			raw_input('[#] Sem mais logins para testar. Pressione ENTER para continuar.')

		except Exception, e:
			print '[-] ERRO 1:', str(e)
			pass


	def isoladas(self):
		try:
			while 1:
#				os.system('clear')
				print '\033[30m'+'[@] Conta:', self.conta.split('@')[0], \
						'({})'.format(str(self.conta.split('@')[1].split('.')[0]).upper())+'\033[0;0m'+'\n'
				print '[#] Mais funções:'
				print
				print '[//] 1. Confirmar solicitações.'
				print '[//] 2. Convidar para página.'
				print '[//] 3. Adicionar amigos.'
				print
				print '[+] 4. [Automatize] Adicionar amigos.'
				print
				print '[&] 0. Voltar'
				print
				opcao = raw_input('[..] Digite a opção:\033[33m ')
				print '\033[0;0m'

				try:
					if int(opcao) == 0:
						return
					elif int(opcao) == 1:
						elm = self.bro.find_elements(By.XPATH, '//button[text()="Confirmar"]')
						len_elm = ((len(elm))-10);random.shuffle(elm);
						if len_elm < 1:break
						calc_convites = 'Menos de 10' if int(len_elm) < 10 else str(len_elm)
						print '\n[$]', calc_convites, 'convites foram carregados. Iniciando...'
						i = 1
						for e in elm:
							print '\r'+'\033[41m[%%] Adicionando %d de %d \33[0;0m' % (i, len_elm),
							sys.stdout.flush()
							i += 1
							try:
								e.send_keys(Keys.RETURN)
								time.sleep(random.choice(self.intervalo))
							except:
								pass
						elm = ''
						raw_input('\n[!] Pressione ENTER para continuar.\n')

					elif int(opcao) == 2:
						elm = self.bro.find_elements(By.XPATH, '//a[@role="checkbox"]')
						len_elm = len(elm);random.shuffle(elm)
						calc_convites = 'Menos de 10' if int(len_elm) < 10 else str(len_elm)
						print '\n[$]', calc_convites, 'convites foram carregados. Iniciando...'
						i = 1
						for e in elm:
							print '\r'+'\033[41m[%%] Adicionando %d de %d \33[0;0m' % (i, len_elm),
							sys.stdout.flush()
							i += 1
							try:
								e.click()
								time.sleep(random.choice(self.intervalo))
							except:
								pass
						elm = ''
						raw_input('\n[!] Pressione ENTER para continuar.\n')

					elif int(opcao) == 3:
#						os.system('clear')
						print '[#] Escolha a velocidade\n'
						print '[///] 1. Rápido'+'\033[30m'+' (Mais ruído)'+'\033[0;0m'
						print '[///] 2. Normal'+'\033[30m'+' (Menos ruído)'+'\033[0;0m'
						opcao = raw_input('\n[..] Escolha uma opção:\033[33m ')
						print '\033[0;0m'

						if int(opcao) == 1:
							elm = self.bro.find_elements(By.XPATH, '//button[text()="Adicionar aos amigos"]')
							len_elm = len(elm);random.shuffle(elm)
							calc_convites = 'Menos de 10' if int(len_elm) < 10 else str(len_elm)
							print '\n[$]', calc_convites, 'convites foram carregados. Iniciando...'
							print '[$] Adicionando amigos...\n'
							# tempoestimado = str(int((int(len(elm))*int(self.tempoadd))/60) < 1 ? 'menos de um':str((int(len(elm))*int(self.tempoadd))/60));
							# tempoestimado = ((len(elm) * self.tempoadd) / 60) < 1 ? 'Menos de um' : str((len(elm) * self.tempoadd) / 60)
							tempoestimado = 'Menos de 1' if ((len(elm) * self.tempoadd) / 60) < 1 else str((len(elm) * self.tempoadd) / 60)
							# print '\033[31m'+'[t] Tempo estimado: '+ tempoestimado +' min.\033[0;0m';
							i = 1
							for e in elm:
								print '\r'+'\033[41m[%%] Adicionando %d de %d \33[0;0m' % (i, len_elm),
								sys.stdout.flush()
								i += 1
								try:
									time.sleep(0)
									e.send_keys(Keys.RETURN)
								except:
									pass

						else:
							elm = self.bro.find_elements(By.XPATH, '//button[text()="Adicionar aos amigos"]')
							len_elm = ((len(elm))-10);random.shuffle(elm)
							calc_convites = 'Menos de 10' if int(len_elm) < 10 else str(len_elm)
							print '\n[$]', calc_convites, 'convites foram carregados. Iniciando...'
							print '[$] Adicionando amigos...\n'
							# tempoestimado = str(int((int(len(elm))*int(self.tempoadd))/60) < 1 ? 'menos de um':str((int(len(elm))*int(self.tempoadd))/60));
							# tempoestimado = ((len(elm) * self.tempoadd) / 60) < 1 ? 'Menos de um' : str((len(elm) * self.tempoadd) / 60)
							tempoestimado = 'Menos de 1' if ((len(elm) * self.tempoadd) / 60) < 1 else str((len(elm) * self.tempoadd) / 60)
							# print '\033[31m'+'[t] Tempo estimado: '+ tempoestimado +' min.\033[0;0m';
							# for e in elm:
							# 	try:
							# 		time.sleep(self.tempoadd)
							# 		e.send_keys(Keys.RETURN)
							# 	except:
							# 		pass
							i = 1
							for el in elm:
								print '\r'+'\033[41m[%%] Adicionando %d de %d \33[0;0m' % (i, len_elm),
								sys.stdout.flush()
								i += 1

								try:
									el.send_keys(Keys.RETURN)
									# time.sleep(random.choice(self.intervalo_adicionar))
									time.sleep(float(str(random.randrange(0,int(self.segundosmax))) +'.'+ str( random.randrange(10))))
									# float(str(random.randrange(5,10)) + '.' + str( random.randrange(10)))

									try:
										confirmar = self.bro.find_elements(By.XPATH, '//button[text()="Confirmar"]')
										for confi in confirmar:
											try:
												confi.send_keys(Keys.RETURN)
											except:
												pass
									except:
										pass

									# try:
									# 	fechar = self.bro.find_elements(By.XPATH, '//button[text()="Fechar"]')
									# 	for fech in fechar:
									# 		try:
									# 			fech.send_keys(Keys.RETURN)
									# 		except:
									# 			pass
									# except:
									# 	pass
								except:
									pass

						# os.system('speaker-test -p 1 -t sine -f 1000 -l 2 2>&1')
						elm = ''
						raw_input('\n[!] Pressione ENTER para continuar.\n')

					elif int(opcao) == 4:
						try:
							urls = [
									'Crescer|https://www.facebook.com/revistacrescer/',
									'Bebe.com.br|https://www.facebook.com/sitebebe/',
									'Revista Pais e Filhos|https://www.facebook.com/paisefilhos/',
									'Mamãe e Papai Coruja|https://www.facebook.com/mamaeepapaicorujas/',
									'Educar para Crescer|https://www.facebook.com/educarcrescer/',
									'Criar Passo a Passo|https://www.facebook.com/criarpassoapasso/',
									'Galinha Pintadinha|https://www.facebook.com/GalinhaPintadinhaPaginaOficial/',
									'Vida de Gestante|https://www.facebook.com/vidadegestanteemae/',
									'Roteiro Baby|https://www.facebook.com/Roteirobaby/',
									'Clube do Brinquedo|https://www.facebook.com/clubedobrinquedo/',
									'Mamatraca|https://www.facebook.com/mamatraca/',
									'Crianças até Jesus|https://www.facebook.com/FernandaMedeirosMeuCantinho/?fref=ts',
									'Mamãe Musa|https://www.facebook.com/blogmamaemusa/?fref=ts',
									'Mamãe Tagarela|https://www.facebook.com/MamaeTagarelaBlog/?fref=ts',
									'Bolsa de Mulher|https://www.facebook.com/bolsa.de.mulher/?ref=timeline_chaining',
									'Mãe.Tips|https://www.facebook.com/MamaeFitnesss/?ref=timeline_chaining',
									]
#							os.system('clear')
							print '[#] Páginas encontradas:\n'
							print '[/] 1. Todas'

							x = 2
							for url in urls:
								print '[/]', str(x) + '.', url.split('|')[0]
								x += 1

							print '\n[&] 0. Sair\n'

							opcao = raw_input('[..] Escolha uma opção:\033[33m ')
							print '\033[0;0m'

							if int(opcao) == 0:
								return

							elif int(opcao) != 1:
								urls_tmp = urls[(int(opcao) - 2)]
								urls = []
								urls.append(urls_tmp)

							random.shuffle(urls)

							for url in urls:
								print '\n[$] Enviando solicitações para página', url.split('|')[0] + '. Aguarde...'
								self.bro.get(url.split('|')[1])
								elm = self.bro.find_elements_by_partial_link_text('pessoas')
								print '[$] Enviando em', str(len(elm)), 'parcelas com', str(self.solicitacoes), 'cada. ('+ str((len(elm) * self.solicitacoes)) +')\n'
								for el in elm:
									try:
										if el != elm[0]:
											el.send_keys(Keys.RETURN)
											time.sleep(5)
											sub = self.bro.find_elements(By.XPATH, '//button[text()="Adicionar aos amigos"]')
											random.shuffle(sub)
											i = 0;j = 1;
											for su in sub:
												try:
													print '\r'+'\033[41m[%%] Adicionando %d de %d \33[0;0m' % (i, int(len(sub))),
													sys.stdout.flush()
													su.send_keys(Keys.RETURN)
													# time.sleep(random.choice(self.intervalo_adicionar))
													time.sleep(float(str(random.randrange(1,5)) +'.'+ str( random.randrange(99))))
													# float(str(random.randrange(5,10)) + '.' + str( random.randrange(10)))
													j += 1

													try:
														confirmar = self.bro.find_elements(By.XPATH, '//button[text()="Confirmar"]')
														for confi in confirmar:
															try:
																confi.send_keys(Keys.RETURN)
															except:
																pass
													except:
														pass

													# try:
													# 	fechar = self.bro.find_elements(By.XPATH, '//button[text()="Fechar"]')
													# 	for fech in fechar:
													# 		try:
													# 			fech.send_keys(Keys.RETURN)
													# 		except:
													# 			pass
													# except:
													# 	pass

													i += 1
													if i > self.solicitacoes:
														el.send_keys(Keys.ESCAPE)
														break
												except:
													pass
											el.send_keys(Keys.ESCAPE)
									except:
										pass

						except Exception, e:
							print '\n[#] ERRO:', str(e)

						raw_input('\n[!] Pressione ENTER para continuar.\n')

					elif int(opcao) == 0:
						return

					elif not int(opcao):
						continue

					else:
						continue

				except:
					return

		except KeyboardInterrupt:
#			os.system('clear')
			print '\n[:)] Obrigado e volte sempre!\n'
			exit(1)

		except:
			return

	def menu(self):
		try:
			while 1:
#				os.system('clear')
				if self.logado:
					print '\033[30m'+'[@] Conta:', self.conta.split('@')[0], \
							'({})'.format(str(self.conta.split('@')[1].split('.')[0]).upper())+'\033[0;0m'+'\n'
				print '[#] Para começar escolha uma opção:\n'
				if not self.logado:
					print '[/] 1. Logar'
					print '[/] 6. Cadastrar'
					print '[/] 7. Checar Logins'
				else:
					print '[/] 2. Convidar para a pagina'
					print '[/] 3. Adicionar amigos'
					print '[/] 4. Confirmar solicitações'
					print '[/] 5. Enviar curtidas'
					print
					print '[+] 8. Mais'
				print '\n[&] 0. Sair'
				print

				opcao = raw_input('[..] Escolha uma opção:\033[33m ')
				print '\033[0;0m'

				if int(opcao) == 1:
					self.logar()
				elif int(opcao) == 7:
					self.checar_login()
				elif int(opcao) == 2:
					self.convidar()
				elif int(opcao) == 3:
					self.adicionar()
				elif int(opcao) == 4:
					self.confirmar()
				elif int(opcao) == 5:
					self.curtir()
				elif int(opcao) == 6:
					self.cadastrar()
				elif int(opcao) == 8:
					self.isoladas()
				elif int(opcao) == 0:
#					os.system('clear')
					if self.logado:
						print '\033[31m'+'\n[!] Saindo de {}, Aguarde...\n\033[0;0m'.format(self.conta)
					else:
						print '\033[31m'+'\n[!] Saindo...\n'+'\033[0;0m'
					time.sleep(1)
					self.bro.close()
					self.logado = False
					continue

				else:
					continue

		except KeyboardInterrupt:
#			os.system('clear')
			print '\n[:)] Obrigado e volte sempre!\n'
			exit(1)

		except:
			pass

def main():
#	os.system('clear')
	f = facebook()
	f.menu()

if __name__ == '__main__':
	main()
