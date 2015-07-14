#--coding: utf8--

from sleekxmpp import ClientXMPP
from celery import shared_task

from conf import settings


class SendMsgBot(ClientXMPP):
    """
    Simple synchronous XMPP bot.
    """
    def jid(self, user):
        return '%s@%s' % (user, self.host)

    def __init__(self, user, password, host, recipients, msg):
        self.recipients = recipients
        self.msg = msg
        self.host = host
        plugin_config = {
            # Enables PLAIN authentication which is off by default.
            'feature_mechanisms': {'unencrypted_plain': True},
        }
        super(SendMsgBot, self).__init__(self.jid(user), password,
                                         plugin_config=plugin_config)
        self.add_event_handler('session_start', self.start)

    def start(self, event):
        self.send_presence()
        self.get_roster()

        for r in self.recipients:
            self.send_message(mto=self.jid(r), mbody=self.msg)

        self.disconnect(wait=True)


@shared_task(name='django_jabber.send_message')
def send_message(message, recipients):
    """
    Send a single message to a list of recipients
    """
    if settings.JABBER_DRY_RUN:
        return
    bot = SendMsgBot(settings.JABBER_USER, settings.JABBER_PASSWORD,
                     settings.JABBER_HOST, recipients, message)
    if bot.connect(use_tls=settings.USE_TLS, use_ssl=settings.USE_SSL):
        bot.process(block=True)
