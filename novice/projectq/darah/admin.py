from django.contrib import admin

# Register your models here.
        # sitetree_urls = [
        #     # Ignore urls.W002. Leading slash is in the right place.
        #     url(r'^/$', redirects_handler, name=get_tree_item_url_name('changelist')),
        #     url(r'^$', redirects_handler, name=get_tree_item_url_name('changelist')),

        #     url(r'^((?P<tree_id>\d+)/)?%sitem_add/$' % prefix_change,
        #         self.admin_site.admin_view(self.tree_admin.item_add), name=get_tree_item_url_name('add')),