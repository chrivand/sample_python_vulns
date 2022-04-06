def update_details(request, acc_id):  
  user = Account.objects.get(acc=acc_id)  
  if request.user.id == user.id:  
    # ALLOW ACTION  
    # VALIDATE REQUEST DATA  
    form = AccountForm(instance=user,request=request)  
    ...  
  else:  
    # DENY ACTION
    raise Exception("User ID of request does not match DB")