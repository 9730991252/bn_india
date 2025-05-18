from bn_india.includes import * 
s =  Session.objects.all()
for session in s:
    data = session.get_decoded()
    if data.get('office_mobile') == mobile:
        Session.objects.filter(session_key=session.session_key).delete()
