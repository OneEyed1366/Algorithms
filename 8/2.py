class Binary_tree:
# Генерация названия ветвей дерева при вызове функции
    def __init__(self, root_obj, child_name="new_child", child_val=None):
        self.tree = {
            child_name: child_val
        }
        self.root = root_obj
# Получение значения корня при вызове в составе функции 'print()'
    def __str__(self):
        return str(self.root)

# Добавление потомка в заданном направлении
    def insert_child(self, new_node, direction):
        if direction in self.tree:
            tree_obj = Binary_tree(new_node)
            tree_obj.tree[direction] = self.tree[direction]
            self.tree[direction] = tree_obj
        else:
            self.tree[direction] = Binary_tree(new_node)

# Получение потомка из заданного направления
    def get_child(self, direction):
        if direction in self.tree:
            print(self.tree[direction])
        else:
            print(self.tree)
# Установка нового корня в заданном направлении
    def set_child_root(self, new_root, direction):
        self.tree[direction].root = new_root

        print(f"Новый root для ветви {direction}: {new_root}")

r = Binary_tree(8)
print(r)
r.get_child("left_child")
r.get_child("right_child")
r.insert_child(4, "left_child")
r.insert_child(12, "right_child")
r.insert_child(15, "middle_child")
r.get_child("left_child")
r.get_child("right_child")
r.get_child("middle_child")
r.set_child_root(111, "middle_child")
r.get_child("middle_child")
