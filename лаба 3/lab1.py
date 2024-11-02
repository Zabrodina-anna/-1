items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']


def find_item_index(litems_list, item_to_find):
    try:
        return litems_list.index(item_to_find)
    except ValueError:
        return None


for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
