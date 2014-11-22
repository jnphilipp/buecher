from django.core import management
from django_cron import CronJobBase, Schedule

class FullCircleMagazineJob(CronJobBase):
	RUN_AT_TIMES = ['12:00']

	schedule = Schedule(run_at_times=RUN_AT_TIMES)
	code = 'books.fullcirclemagazine'

	def do(self):
		management.call_command('fullcircle')

class FreiesMagazinJob(CronJobBase):
	RUN_AT_TIMES = ['12:00']

	schedule = Schedule(run_at_times=RUN_AT_TIMES)
	code = 'books.freiesMagazin'

	def do(self):
		management.call_command('freiesMagazin')