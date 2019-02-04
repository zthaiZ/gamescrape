import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':

	consoles=['3ds','android','iphone','pc','ps3','ps4','switch','vita','xbox360','xboxone']
	
	valid=False
	while(valid==False):
		choice=input("For which console would you like to check the top games?")
		if choice.lower() not in consoles:
			print('Sorry, this console is not one of the available choices. Please try a valid console:')
			print('3DS\nAndroid\niPhone\nPC\nPS3\nPS4\nSwitch\nVita\nXbox360\nXboxOne')
		else:
			valid=True

	url='https://www.gamefaqs.com/'+choice
	response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
	soup = BeautifulSoup(response.content,'html.parser')

	top=soup.find_all(string = 'Top 10 Games')[0].find_parents()[2]
	for i in top.find('ol').find_all('li'):
		print(' '.join((i.get_text()).strip().split()))