import random
#https://mail.google.com/mail/u/0/#inbox/FMfcgzGsmNMjdgczfXgsGpVKPdKvJhJG
frens = []
for i in range(5):
	frne = input("Tell me 5 of your friend in order form 1(best) to 5. Press enter after each friend")
	frens.append(frne)
print(frens)
print(frens[0])
print(frens[4])
frens.sort()
print(frens)