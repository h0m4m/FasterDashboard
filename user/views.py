from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .models import User, Contract, Fine, Driver
from datetime import date
from django.db.models import Sum
from datetime import date, timedelta
from django.urls import reverse



def home(request):
    return redirect('user')

def user(request):
    return render(request, 'user/user.html')


def user_details(request):
    user_id = request.GET.get('user_id')
    try:
        user = User.objects.get(id=user_id)
        contracts = Contract.objects.filter(user=user)
        
        # Get fines related to the contracts of this user
        fines = Fine.objects.filter(contract__in=contracts)
        
        today = date.today()

        # Calculate remaining days, update contract activity, and calculate hold release date
        for contract in contracts:
            remaining_days = (contract.return_date - today).days
            if remaining_days >= 0:
                contract.remaining_days = remaining_days
            else:
                contract.is_active = False
                contract.save()

            # Calculate hold release date
            business_days_to_add = 21
            current_date = contract.return_date
            while business_days_to_add > 0:
                current_date += timedelta(days=1)
                if current_date.weekday() < 5:  # Monday to Friday (0 to 4)
                    business_days_to_add -= 1
            contract.hold_release_date = current_date
            contract.save()

            # Check if today matches the hold_release_date and update deposit_status
            if today == contract.hold_release_date:
                Contract.objects.filter(id=contract.id).update(deposit_status=False)

        # Sort contracts based on 'is_active', True values first
        contracts = sorted(contracts, key=lambda x: not x.is_active)
        total_fines = fines.count()  # Get total fines count

        return render(request, 'user/user_details.html', {'user': user, 'contracts': contracts, 'total_fines': total_fines})
    except User.DoesNotExist:
        return render(request, 'user/user_not_found.html')

def contract_fines(request, contract_id):
    contract = Contract.objects.get(id=contract_id)
    fines = Fine.objects.filter(contract=contract)

    total_fines = fines.count()  # Get total fines count
    total_amount = fines.aggregate(Sum('amount'))['amount__sum'] or 0  # Get total amount

    return render(request, 'user/contract_fines.html', {
        'contract': contract,
        'fines': fines,
        'total_fines': total_fines,
        'total_amount': total_amount,
    })

def driver(request):
    return render(request, 'driver/driver.html')

def driver_dashboard(request):
    driver_id = request.GET.get('driver_id')
    try:
        driver = Driver.objects.get(id=driver_id)
        active_contracts = Contract.objects.filter(is_active=True)
        active_contracts = sorted(active_contracts, key=lambda x: not x.is_active)

        return render(request, 'driver/driver_dashboard.html', {'driver': driver, 'active_contracts': active_contracts})
    except Driver.DoesNotExist:
        return render(request, 'driver/driver_not_found.html')
    
def contract_condition_report(request, contract_id):
    contract = get_object_or_404(Contract, pk=contract_id)
    driver_id = request.GET.get('driver_id')

    if request.method == 'POST':
        # Handle form submission
        for field_name in ['car_exterior_image1', 'car_exterior_image2', 'car_exterior_image3', 'car_exterior_image4', 'car_exterior_image5',
                           'car_interior_image1', 'car_interior_image2', 'car_interior_image3', 'car_interior_image4', 'car_interior_image5']:
            image_file = request.FILES.get(field_name)
            if image_file:
                setattr(contract, field_name, image_file)
        
        # Save the updated contract with new image paths
        contract.save()

        # Redirect based on the driver_id
        if driver_id:
            redirect_url = reverse('driver_dashboard') + f'?driver_id={driver_id}'
        else:
            redirect_url = '/'  # Redirect to home if driver_id is not available
        
        return redirect(redirect_url)

    return render(request, 'user/contract_condition_report.html', {'contract': contract})