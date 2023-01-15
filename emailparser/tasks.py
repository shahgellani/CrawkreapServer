from django.utils.timezone import localtime
from django.utils import timezone

from celery import shared_task
from utils.readEmail import ReadEmail


@shared_task(name="email_parser")
def email_parser():
    try:
        print("Testing")
        # ReadEmail.read_email()
        # current_time = localtime(timezone.now())
        # bots_list = Bot.objects.filter(
        #     start_date_time__lte=current_time, end_date_time__gte=current_time
        # )
        # for bot in bots_list:
        #     time_left = localtime(bot.end_date_time) - current_time
        #     fetched_interval_from_time_left = int(str(time_left).split(":")[1])
        #     if fetched_interval_from_time_left % bot.schedule_interval == 0:
        #         run_task(bot=bot, data="Data")
    except Exception as e:
        print("Exception occurs in check_bots_tobe_run task. Error: {}".format(str(e)))


# @shared_task(name="check_status_of_bots")
# def check_status_of_bots():
#     logger_message = ""
#     # account_sid = 'AC2de902bfa4d8a2f9e9d1b9834f95ef91'
#     # auth_token = '10a5ab56bb65d20a35a720049f11285f'
#     # client = Client(account_sid, auth_token)
#     try:
#         current_time = localtime(timezone.now())
#         bots_in_progress = Bot.objects.filter(
#             start_date_time__lte=current_time, end_date_time__gte=current_time
#         )
#         bots_not_started_yet = Bot.objects.filter(start_date_time__gte=current_time)
#         bot_completed = Bot.objects.filter(
#             start_date_time__lte=current_time, end_date_time__lte=current_time
#         )
#         bots = Bot.objects.all()
#         for bot in bots_in_progress:
#             bot.bot_status = "IN_PROGRESS"
#             bot.save(update_fields=["bot_status"])
#         for bot in bots_not_started_yet:
#             bot.bot_status = "NOT_STARTED"
#             bot.save(update_fields=["bot_status"])
#         for bot in bot_completed:
#             if bot.bot_status != "ABORTED":
#                 bot.bot_status = "FINISHED"
#                 bot.save(update_fields=["bot_status"])
#         for bot in bots:
#             start_seconds_left = (
#                 current_time - localtime(bot.start_date_time)
#             ).total_seconds()
#             if float(5) >= start_seconds_left > 0:
#                 LOGGER.info(start_seconds_left)
#                 LOGGER.info("Bot Started")
#                 requests.post(
#                     "http://0.0.0.0:8000/notifications/create-celery-notification",
#                     json={"title": "Bot_Status", "body": "Bot Started"},
#                 )
#                 requests.post(
#                     "http://0.0.0.0:8000/notifications/create-celery-notification",
#                     json={"title": "Update_Bots_List", "body": ""},
#                 )
#             end_seconds_exceed = (
#                 current_time - localtime(bot.end_date_time)
#             ).total_seconds()
#             if float(5) >= end_seconds_exceed > 0:
#                 LOGGER.info(end_seconds_exceed)
#                 LOGGER.info("Bot Stopped")
#                 requests.post(
#                     "http://0.0.0.0:8000/notifications/create-celery-notification",
#                     json={"title": "Bot_Status", "body": "Bot Stopped"}
#                 )
#                 requests.post(
#                     "http://0.0.0.0:8000/notifications/create-celery-notification",
#                     json={"title": "Update_Bots_List", "body": ""},
#                 )
#             logger_message = "Check Status of bots executed successfully"
#     except Exception as e:
#         logger_message = "Check status of Bots got exception. Error: {}".format(str(e))
#     finally:
#         LOGGER.info(logger_message)
