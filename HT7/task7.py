'''НT7.7.   7. Напишіть функцію, яка приймає 2 списки. Результатом має
 бути новий список, в якому знаходяться елементи першого списку, яких
  немає в другому. Порядок елементів, що залишилися має відповідати порядку
  в першому (оригінальному) списку. Реалізуйте обчислення за допомогою
   генератора    в один рядок.
    Приклад:
    array_diff([1, 2], [1]) --> [2]
    array_diff([1, 2, 2, 2, 3, 4], [2]) --> [1, 3, 4]'''


def my_function(list_1, list_2):

    result = [element for element in list_1 if element not in list_2]
    return result


print(my_function([1, 2, 2, 2, 3, 4], [2]))