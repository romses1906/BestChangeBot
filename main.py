from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from config import BOT_TOKEN
from keyboard import exchangers_keyboard, ids_callback_factory, rates_BTC_USDT
from requests_api import exchangers
import logging

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO, format="%(levelname)-8s [%(asctime)s] %(message)s")
dp.middleware.setup(LoggingMiddleware())


async def set_default_commands(dp: Dispatcher) -> None:
    """
    Функция создания команд в меню бота

    :param dp: Dispatcher
    :return: None
    """
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
    ])


@dp.message_handler(commands=['start'])
async def command_start_handler(message: types.Message) -> None:
    """
    Хэндлер команды 'start', выводит на экран сообщение с предложением выбора обменника
    и inline-клавиатуру, содержащую названия обменников

    :param message: Message - сообщение от пользователя с командой 'start'
    :return: None
    """
    logging.info(f'Пользователь {message.from_user.id} выбрал команду: {message.text}')
    await message.answer(text='Выберите обменник:', reply_markup=exchangers_keyboard)


@dp.callback_query_handler(ids_callback_factory.filter())
async def exchanger_cb_handler(
        callback: types.CallbackQuery,
        callback_data: dict) -> None:
    """
    Обработчик inline-кнопок с выбором обменника. В результате выбора обменника выводится сообщение
    с разницей в курсе с обменником, занимающим первое место в списке

    :param callback: CallbackQuery - выбранный пользователем обменник
    :param callback_data: dict - словарь, содержащий id обменника
    :return: None
    """
    for val in rates_BTC_USDT:
        if val['exchange_id'] == int(callback_data['value']):
            name_selected_exchanger = exchangers[val['exchange_id']]['name']
            name_first_exchanger = exchangers[rates_BTC_USDT[0]['exchange_id']]['name']
            logging.info(f'Пользователь {callback.from_user.id} выбрал обменник {name_selected_exchanger}')
            await bot.send_message(callback.from_user.id,
                                   '{}'.format(round((rates_BTC_USDT[0]['get'] - val['get']), 4)))
            logging.info(
                'Разница в курсе с первым обменником в списке {name_first_exchanger} составляет {difference}'.format(
                    name_first_exchanger=name_first_exchanger,
                    difference=round((rates_BTC_USDT[0]['get'] - val['get']), 4)))


@dp.message_handler()
async def echo(message: types.Message):
    """
    Эхо-хендлер, куда поступают текстовые сообщения от пользователя без указанного состояния

    :param message: Message - сообщение от пользователя без указанного состояния
    :return: None
    """
    logging.info(f'Пользователь {message.from_user.id} ввел сообщение: {message.text}')
    await message.answer('Выберите обменник из списка выше')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=set_default_commands)



