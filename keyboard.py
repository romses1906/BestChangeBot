from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from requests_api import exchangers, rates

rates_BTC_USDT: list[dict[str, float | int]] = rates(curr_from=93, curr_to=10)

ids_callback_factory = CallbackData('id', 'value')

exchangers_keyboard = InlineKeyboardMarkup(resize_keyboard=True)

for val in rates_BTC_USDT:
    exchangerButton = InlineKeyboardButton(
        text='{name}'.format(name=exchangers[val['exchange_id']]['name']),
        callback_data=ids_callback_factory.new(value=val['exchange_id']))
    exchangers_keyboard.add(exchangerButton)
