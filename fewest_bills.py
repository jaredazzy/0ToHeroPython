#This part of the code gets the initial amount of how much the user wants to withdraw
withdraw_amount = int(input('Please enter the amount of money you wish to withdraw:'))

#This part of the code keeps track of hundred bills received and new amount once hundred values are subtracted
hundredbill_received = withdraw_amount // 100
total_amount_hunsubtracted = withdraw_amount - (hundredbill_received * 100)

#This part of the code keeps track of fifties received and new amount once hundred, and fifty values are subtracted
fifties_received = total_amount_hunsubtracted // 50
total_amount_fifsubtracted = total_amount_hunsubtracted - (fifties_received * 50)

#This part of the code keeps track of twenties received and new amount once hun, fif, and twen values are subtracted
twenties_received = total_amount_fifsubtracted // 20
total_amount_twensubtracted = total_amount_fifsubtracted - (twenties_received * 20)

#This part of the code keeps track of tens received and new amount once hun,fif,twen,ten values are subtracted
ten_received = total_amount_twensubtracted // 10
total_amount_tensubtracted = total_amount_twensubtracted - (ten_received * 10)

#This part of the code keeps track of fives received, and new amount once hun,fif,twen,ten, and five vals are subtracted
five_received = total_amount_tensubtracted // 5
total_amount_fivesubtracted = total_amount_tensubtracted - (five_received * 5)

#This part of the code keeps track of ones received
one_received = total_amount_fivesubtracted // 1

#This part of the code prints out the total amount of each bill they receive.
print(f'You received ', hundredbill_received, 'hundred(s)')
print(f'You received ', fifties_received, 'fifty(s)')
print(f'You received ', twenties_received, 'twenty(s)')
print(f'You received ', ten_received, 'ten(s)')
print(f'You received ', five_received, 'five(s)')
print(f'You received ', one_received, 'one(s)')


