# from accounts.models import *
# u1 = User.objects.create_user(username='Andrey')
# u2 = User.objects.create_user(username='Petr')
# Author.objects.create(authorUser=u1)
# Author.objects.create(authorUser=u2)
# Category.objects.create(name='IT')
# Category.objects.create(name='Politics')
# Category.objects.create(name='Economy')
# Category.objects.create(name='Cars')
# author = Author.objects.get(id=1)
# Post.objects.create(author=author, categoryType='NW', title='sometitle', text='somebigtext')
# Post.objects.create(author=author, categoryType='AR', title='Hello World', text='Hello!')
# author = Author.objects.get(id=2)
# Post.objects.create(author=author, categoryType='AR', title='Goodbye World', text='Goodbye!')
# Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
# Post.objects.get(id=2).postCategory.add(Category.objects.get(id=2))
# Post.objects.get(id=2).postCategory.add(Category.objects.get(id=3))
# Post.objects.get(id=4).postCategory.add(Category.objects.get(id=4))
# Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='anytextbyauthor')
# Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=2).authorUser, text='anytext')
# Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=1).authorUser, text='good day!')
# Comment.objects.create(commentPost=Post.objects.get(id=5), commentUser=Author.objects.get(id=2).authorUser, text='good night!')
# Comment.objects.get(id=1).like()
# Comment.objects.get(id=2).like()
# Comment.objects.get(id=3).like()
# Comment.objects.get(id=4).like()
# Post.objects.get(id=1).like()
# Post.objects.get(id=2).like()
# Post.objects.get(id=5).like()
# Post.objects.get(id=5).dislike()
# Post.objects.get(id=5).rating
# Author.objects.get(id=1)
# a = Author.objects.get(id=1)
# a.update_rating()
# a.ratingAuthor
# Author.objects.get(id=2)
# b = Author.objects.get(id=2)
# b.update_rating()
# b.ratingAuthor
# a = Author.objects.order_by('-ratingAuthor')[:1]
# for i in a:
# i.ratingAuthor
# i.authorUser.username
# a = Post.objects.order_by('-rating')[:1]
# for i in a:
# i.dateCreation
# i.rating
# i.title
# i.text
# a = Comment.objects.order_by('-rating')[:1]
# for i in a:
# i.dateCreation
# i.commentUser
# i.rating
# i.text