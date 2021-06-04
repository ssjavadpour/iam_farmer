class Vendor:
    def __init__(self,vendor_id, name, username,products,bins, orders,locations):
        self.vendor_id = vendor_id #unique identfier for vendor
        self.name = name
        self.username = username
        self.products = products #list of unique product types available to the vendor
        self.bins = bins #list of unique bin_ids belonging to vendor 
        self.orders = orders #list of all order_ids placed with vendor ##SUBJECT TO REFACTORING
        self.locations = locations #list of location_ids that contain vendor product/bins


class Product:
    def __init(self, product_id, product_type, unit_price, unit_measure, unit_weight):
        self.product_id = product_id 
        self.product_type = product_type
        self.unit_price = unit_price
        self.unit_measure = unit_measure
        self.unit_weight = unit_weight


class Order:
    def __init__(self, order_id, order_items, status, vendor, customer, fulfillment_time, history):
        self.order_id = order_id #unique identifier
        self.order_items = order_items #list of order_item_ids 
        self.status = status #pending/completed/new
        self.vendor = vendor #vendor_id responsible for fulfilling the order
        self.customer = customer #simple name to identify customer name, can be replaced with customer_id if the app expands
        self.fulfillment_time = fulfillment_time #sum of order_items[i].fulfillment_time
        self.history = history #list of order_history objects ##SUBJECT TO REFACTORING

class Bin:
    def __init__(self,number,location,product,owner,product_count,status,total_weight):
        self.number = number #unique bin_id
        self.location = location #unique location_id
        self.product = product #unique product_id ##each bin can only hold one type of product
        self.owner = owner #unique vendor_id
        self.product_count = product_count #how many product items are in bin. gets updated after each fulfilled order/transaction
        self.status = status #in_stock/low_inventory/out_of_stock
        self.total_weight = total_weight #product_count*product.unit_weight ##SUBJECT TO REFACTORING


