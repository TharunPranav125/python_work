people = ['bhargavi','harine','sandy']
message_1 = f'Hello!!{people[0].title()},You are invited to dinner'
message_2 = f'Hello!!{people[1].title()},You are invited to dinner'
message_3 = f'Hello!!{people[2].title()},You are invited to dinner\n'
print(message_1)
print(message_2)
print(message_3)

removed_people = people.pop(2)
print(f'{removed_people.title()} could not make it!!')

people.insert(2,'charan')
print(f"Instead of {removed_people.title()},{people[2].title()} could come")
message_3 = f'Hello!!{people[2].title()},You are invited to dinner\n'
print(message_1)
print(message_2)
print(message_3)

people.insert(0,'patricia')
people.insert(2,'dheekshithan')
people.append('sandy')
message_1 = f'Hello!!{people[0].title()},You are invited to dinner'
message_2 = f'Hello!!{people[1].title()},You are invited to dinner'
message_3 = f'Hello!!{people[2].title()},You are invited to dinner'
message_4 = f'Hello!!{people[3].title()},You are invited to dinner'
message_5 = f'Hello!!{people[4].title()},You are invited to dinner'
message_6 = f'Hello!!{people[5].title()},You are invited to dinner'
print(people)

print(message_1)
print(message_2)
print(message_3)
print(message_4)
print(message_5)
print(message_6)

message = "Only two people are invited!!"
print(message)

removed_people_1 = people.pop(0)
removed_people_2 = people.pop(1)
removed_people_3 = people.pop(2)
removed_people_4 = people.pop(2)

print(f'{removed_people_1.title()}!!Sorry You are not invited!!')
print(f'{removed_people_2.title()}!!Sorry You are not invited!!')
print(f'{removed_people_3.title()}!!Sorry You are not invited!!')
print(f'{removed_people_4.title()}!!Sorry You are not invited!!\n')
print(f'{people[0]}!!You are invited to dinner')
print(f'{people[1]}!!You are invited to dinner')




