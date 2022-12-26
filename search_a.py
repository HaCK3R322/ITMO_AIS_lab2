# A* поиск
# Возвращает кратчайший путь и список посещенных вершин в порядке обхода

def search_a(graph, start, end):
    # Проверка на валидность входных данных
    if start not in graph or end not in graph:
        raise ValueError('Начальная или конечная вершина не найдена')

    # Словарь, где ключ - вершина, значение - родительская вершина
    parent = {start: None}
    # Список посещенных вершин
    visited = []
    # Словарь, где ключ - вершина, значение - стоимость пути
    cost = {start: 0}
    # Список вершин для обработки
    queue = [start]

    # Пока есть вершины для обработки
    while len(queue) > 0:
        # Выбор вершины с минимальной стоимостью пути
        current = min(queue, key=lambda x: cost[x])
        # Если вершина - конечная, то поиск окончен
        if current == end:
            break

        # Удаление вершины из списка для обработки
        queue.remove(current)
        # Добавление вершины в список посещенных вершин
        visited.append(current)

        # Перебор смежных вершин
        for neighbor in graph[current]:
            # Стоимость пути до смежной вершины
            new_cost = cost[current] + graph[current][neighbor]['weight']
            # Если смежная вершина еще не была посещена или
            # стоимость пути до нее меньше, чем ранее рассчитанная
            if neighbor not in cost or new_cost < cost[neighbor]:
                # Обновление стоимости пути до смежной вершины
                cost[neighbor] = new_cost
                # Добавление смежной вершины в список для обработки
                queue.append(neighbor)
                # Обновление родительской вершины
                parent[neighbor] = current

    # Восстановление пути
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]

    # Путь в обратном порядке
    path.reverse()

    return path, visited