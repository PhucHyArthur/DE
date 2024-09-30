from django.http import JsonResponse
import asyncio

# Async view example
async def async_view(request):
    await asyncio.sleep(2)  # Giả lập một tác vụ tốn thời gian
    return JsonResponse({'message': 'Async view response after 2 seconds'})
