from datetime import datetime
import instaloader

#Carrega a biblioteca e faz login na conta
l = instaloader.Instaloader()
l.login('Login da conta que sera utlizada pelo programa','Senha da conta que sera utlizada pelo programa')

#Carrega todos os posts do perfil
posts = instaloader.Profile.from_username(l.context, "conta a qual tera os posts baixados").get_posts()

#Periodo dentro do qual os posts serão baixados
SINCE = datetime(2021,1,16) #Data inicial para o download dos posts
UNTIL = datetime(2021,6,18) #Data final para o download dos posts

#Percorre os posts e baixa apenas os que estão dentro do periodo desejado
for post in posts:
        if(post.date >= SINCE) and (post.date <= UNTIL):
            print(post.date)
            l.download_post(post, "ista-posts-donwloads")