from django.shortcuts import render, redirect
from home.models import User
from django.contrib import messages

# Create your views here.
def transactions(request):

	objects = User.objects.all()

	dic = {}
	names = []
	for i in objects:
		names.append(i.user)
	print(names)
	dic['names'] = names

	return render(request,'transactions/trans.html',dic)

def users(request):
	if request.method == "POST":
		user1 = request.POST.get('user1')
		user2 = request.POST.get('user2')
		print(user1)
		print(user2)
		if user1==user2:
			print('message should come here')
			messages.success(request, "You can not do transactions between same accounts.")
			return redirect('transactions')
		else:
			amount = request.POST.get('amount')
			print(amount)
			a = User.objects.get(user=user1)
			print(a.balance)

			if a.balance < int(amount) :
				messages.success(request, "You can not do transaction because you don't have enough balance.")
				return redirect('transactions')

			else:
				a.balance = a.balance - int(amount)
				a.save()
				b = User.objects.get(user=user2)
				b.balance = b.balance + int(amount)
				b.save()



	objects = User.objects.all()

	dic = {}
	names = []
	amounts = []
	range = []
	temp = 0
	for i in objects:
		# amounts.append(i.balance)
		names.append([i.user,i.balance])
		# range.append(temp)

		temp = temp + 1
		# names[i.user] = i.balance


	print(names)
	# print(amounts)
	print(range)
	dic['names'] = names
	# dic['amounts'] = amounts
	# dic['range'] = range
	return render(request,'transactions/users.html',dic)
