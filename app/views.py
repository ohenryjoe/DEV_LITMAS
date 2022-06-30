from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def about(request):
    return render(request, 'about.html')


def accordion(request):
    return render(request, 'accordion.html')


def alerts(request):
    return render(request, 'alerts.html')


def avatar(request):
    return render(request, 'avatar.html')


def background(request):
    return render(request, 'background.html')


def badge(request):
    return render(request, 'badge.html')


def blog_details(request):
    return render(request, 'blog-details.html')


def blog_edit(request):
    return render(request, 'blog-edit.html')


def blog(request):
    return render(request, 'blog.html')


def border(request):
    return render(request, 'border.html')


def breadcrumbs(request):
    return render(request, 'breadcrumbs.html')


def buttons(request):
    return render(request, 'buttons.html')


def calendar2(request):
    return render(request, 'calendar2.html')


def cards(request):
    return render(request, 'cards.html')


def carousel(request):
    return render(request, 'carousel.html')


def cart(request):
    return render(request, 'cart.html')


def chart_chartjs(request):
    return render(request, 'chart-chartjs.html')


def chart_echart(request):
    return render(request, 'chart-echart.html')


def chart_flot(request):
    return render(request, 'chart-flot.html')


def chart_morris(request):
    return render(request, 'chart-morris.html')


def chart_nvd3(request):
    return render(request, 'chart-nvd3.html')


def chat(request):
    return render(request, 'chat.html')


def checkout(request):
    return render(request, 'checkout.html')


def client_create(request):
    return render(request, 'client-create.html')


def clients(request):
    return render(request, 'clients.html')


def colors(request):
    return render(request, 'colors.html')


def construction(request):
    return render(request, 'construction.html')


def counters(request):
    return render(request, 'counters.html')


def datatable(request):
    return render(request, 'datatable.html')


def display(request):
    return render(request, 'display.html')


def dropdown(request):
    return render(request, 'dropdown.html')


def empty(request):
    return render(request, 'empty.html')


def error404(request):
    return render(request, 'error404.html')


def error500(request):
    return render(request, 'error500.html')


def error501(request):
    return render(request, 'error501.html')


def faq(request):
    return render(request, 'faq.html')


def file_attachments(request):
    return render(request, 'file-attachments.html')


def file_manager_1(request):
    return render(request, 'file-manager-1.html')


def file_manager_2(request):
    return render(request, 'file-manager-2.html')


def file_manager(request):
    return render(request, 'file-manager.html')


def flex(request):
    return render(request, 'flex.html')


def footers(request):
    return render(request, 'footers.html')


def forgot_password(request):
    return render(request, 'forgot-password.html')


def form_advanced(request):
    return render(request, 'form-advanced.html')


def form_editable(request):
    return render(request, 'form-editable.html')


def form_elements(request):
    return render(request, 'form-elements.html')


def form_layouts(request):
    return render(request, 'form-layouts.html')


def form_validation(request):
    return render(request, 'form-validation.html')


def form_wizard(request):
    return render(request, 'form-wizard.html')


def gallery(request):
    return render(request, 'gallery.html')


def height(request):
    return render(request, 'height.html')


def icons(request):
    return render(request, 'icons.html')


def icons2(request):
    return render(request, 'icons2.html')


def icons3(request):
    return render(request, 'icons3.html')


def icons4(request):
    return render(request, 'icons4.html')


def icons5(request):
    return render(request, 'icons5.html')


def icons6(request):
    return render(request, 'icons6.html')


def icons7(request):
    return render(request, 'icons7.html')


def icons8(request):
    return render(request, 'icons8.html')


def icons9(request):
    return render(request, 'icons9.html')


def icons10(request):
    return render(request, 'icons10.html')


@login_required
def index(request):
    return render(request, 'index.html')


def invoice_create(request):
    return render(request, 'invoice-create.html')


def invoice_details(request):
    return render(request, 'invoice-details.html')


def invoice_edit(request):
    return render(request, 'invoice-edit.html')


def invoice_list(request):
    return render(request, 'invoice-list.html')


def invoice_timelog(request):
    return render(request, 'invoice-timelog.html')


def landing(request):
    return render(request, 'landing.html')


def loaders(request):
    return render(request, 'loaders.html')


def lockscreen(request):
    return render(request, 'lockscreen.html')


def login(request):
    return render(request, 'login.html')


def mail_compose(request):
    return render(request, 'mail-compose.html')


def mail_inbox(request):
    return render(request, 'mail-inbox.html')


def mail_read(request):
    return render(request, 'mail-read.html')


def mail_settings(request):
    return render(request, 'mail-settings.html')


def maps(request):
    return render(request, 'maps.html')


def maps1(request):
    return render(request, 'maps1.html')


def maps2(request):
    return render(request, 'maps2.html')


def margin(request):
    return render(request, 'margin.html')


def mediaobject(request):
    return render(request, 'mediaobject.html')


def modal(request):
    return render(request, 'modal.html')


def navigation(request):
    return render(request, 'navigation.html')


def notify(request):
    return render(request, 'notify.html')


def offcanvas(request):
    return render(request, 'offcanvas.html')


def opacity(request):
    return render(request, 'opacity.html')


def padding(request):
    return render(request, 'padding.html')


def pagination(request):
    return render(request, 'pagination.html')


def panels(request):
    return render(request, 'panels.html')


def position(request):
    return render(request, 'position.html')


def pricing(request):
    return render(request, 'pricing.html')


def product_details(request):
    return render(request, 'product-details.html')


def products(request):
    return render(request, 'products.html')


def profile(request):
    return render(request, 'profile.html')


def progress(request):
    return render(request, 'progress.html')


def project_details(request):
    return render(request, 'project-details.html')


def project_edit(request):
    return render(request, 'project-edit.html')


def project_new(request):
    return render(request, 'project-new.html')


def projects_list(request):
    return render(request, 'projects-list.html')


def projects(request):
    return render(request, 'projects.html')


def rangeslider(request):
    return render(request, 'rangeslider.html')


def rating(request):
    return render(request, 'rating.html')


def register(request):
    return render(request, 'register.html')


def scroll(request):
    return render(request, 'scroll.html')


def services(request):
    return render(request, 'services.html')


def settings(request):
    return render(request, 'settings.html')


def sweetalert(request):
    return render(request, 'sweetalert.html')


def switcherpage(request):
    return render(request, 'switcherpage.html')


def table_editable(request):
    return render(request, 'table-editable.html')


def tables(request):
    return render(request, 'tables.html')


def tabs(request):
    return render(request, 'tabs.html')


def tags(request):
    return render(request, 'tags.html')


def task_create(request):
    return render(request, 'task-create.html')


def task_edit(request):
    return render(request, 'task-edit.html')


def tasks_list(request):
    return render(request, 'tasks-list.html')


def terms(request):
    return render(request, 'terms.html')


def thumbnails(request):
    return render(request, 'thumbnails.html')


def ticket_details(request):
    return render(request, 'ticket-details.html')


def timeline(request):
    return render(request, 'timeline.html')


def tooltipandpopover(request):
    return render(request, 'tooltipandpopover.html')


def treeview(request):
    return render(request, 'treeview.html')


def typography(request):
    return render(request, 'typography.html')


def users_list(request):
    return render(request, 'users-list.html')


def width(request):
    return render(request, 'width.html')


def wishlist(request):
    return render(request, 'wishlist.html')


def wysiwyag(request):
    return render(request, 'wysiwyag.html')
