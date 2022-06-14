Macchanger basicamente muda seu MAC Address da sua placa de rede ethernet/wifi.

1-Instalação 
	sudo su apt install macchanger -y

2-macchanger -h para opções e sintaxe.

3-Podemos validar nosso mac address digitando 
	macchanger -s wlan0 (lembrando que no exemplo foi usado a placa wi-fi)

4-Para alterar efetivamente, vamos ver a placa de rede que queremos alterar e digitarmos :
	ifconfig wlan 0 down
	macchanger -a wlan0 (a opção 'a' nos da um mac randomico).
	macchanger -p wlan0	
	ifconfig wlan0 up
5-Apos isso vamos estar operando com o novo mac.

*Existe alternativas para automatizar isso no reboot do OS por exemplo criando um bash.

