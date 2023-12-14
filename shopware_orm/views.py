from django.http import HttpResponse

from .models import TestShopwareModel


def testview(request):
    instance = TestShopwareModel.api.create(id=1, name="test", active=True)

    query = TestShopwareModel.api.filter(id=instance.id)

    return HttpResponse(f"<pre>"
                        f"{instance.json()}\n\n"
                        f"{query}"
                        f"</pre>")
