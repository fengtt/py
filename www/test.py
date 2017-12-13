import sys
import orm,asyncio
from models import User, Blog, Comment

@asyncio.coroutine
def test(loop):
        yield from orm.create_pool(loop=loop, user='root', password='root', db='awesome')
        u = User(name='Test', email='test@example.comssssss', passwd='1234567890', image='about:blank')
        yield from u.save()
        yield from orm.destory_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()