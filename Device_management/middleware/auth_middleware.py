class AuthRequiredMiddleware(object):
    def process_request(self, request):
    	print("dsa")
        # if not request.user.is_authenticated():
        #     return HttpResponseRedirect(reverse('landing_page')) # or http response
        # return None