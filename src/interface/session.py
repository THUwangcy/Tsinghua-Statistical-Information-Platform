def add_session(request, *args, **kw):
    # request.session.set_expiry()
    print 'add_session: ', kw
    for (key, value) in kw.items():
        request.session[key] = value


def del_session(request):
    try:
        del request.session['username']
        del request.session['identity']
        del request.session['email']
        del request.session['student_id']
    except KeyError:
        pass


def del_email(request):
    try:
        del request.session['email']
    except KeyError:
        pass


def get_student_id(request):
    if 'student_id' in request.session:
        return request.session['student_id']
    return 'none'


def get_username(request):
    if 'username' in request.session:
        return request.session['username']
    return 'none'


def get_identity(request):
    if 'identity' in request.session:
        return request.session['identity']
    return 'none'


def get_email(request):
    if 'email' in request.session:
        return request.session['email']
    return 'none'
