from bestchange_api import BestChange

api = BestChange()
exchangers: dict = api.exchangers().get()


def rates(curr_from: int, curr_to: int) -> list[dict[str, float | int]]:
    """
    Функция для получения курсов валют, отфильтрованных и отсортированных по направлению
    из валюты с id = curr_from в валюту с id = curr_to

    :param curr_from: int - id валюты, которую пользователь хочеть продать
    :param curr_to: int - id валюты, которую пользователь хочеть получить

    :return: list[dict[str, float | int]] - курсы валют, отфильтрованные и отсортированные по заданному направлению
    """

    return api.rates().filter(curr_from, curr_to)
