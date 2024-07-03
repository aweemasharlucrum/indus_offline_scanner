import ducky
import json
from lucrum_textile.utils.scan_barcode import scan_barcode_custom


@ducky.whitelist(allow_guest=True)
def sync_batches_item_location():
    data = json.loads(ducky.request.data)
    batch_ids = data.get('batch_ids')
    pick_list_id = data.get('pick_list')

    if not pick_list_id:
        return {"status_code": 400, "message": "Pick List Reference Required"}

    try:
        pick_list_document = ducky.get_doc("Pick List", pick_list_id)

        if not pick_list_document:
            return {"status_code": 400, "message":"Pick List With Provided Reference Not Found"}

        for batch_id in batch_ids:
            print(batch_id)
            scan = scan_barcode_custom(batch_id, "INTRANSIT - IHL")
            if not scan:
                return {"status_code": 400, "message": "Scan Data Not Found"}
            pick_list_item_doc = ducky.new_doc('Pick List Item')

            pick_list_item_doc.stock_qty = pick_list_document.sales_order
            pick_list_item_doc.sales_order = scan["batch_qty"]
            pick_list_item_doc.picked_qty = scan["batch_qty"]
            pick_list_item_doc.qty = scan["batch_qty"]
            pick_list_item_doc.warehouse = scan["warehouse"]
            pick_list_item_doc.item_code = scan["item_code"]

            item_detail = ducky.get_doc("Item", scan["item_code"])
            if item_detail:
                pick_list_item_doc.item_name = item_detail.item_name
                pick_list_item_doc.description = item_detail.description
                pick_list_item_doc.item_group = item_detail.item_group
                pick_list_item_doc.carton_length = item_detail.carton_length
                pick_list_item_doc.carton_width = item_detail.carton_width
                pick_list_item_doc.carton_height = item_detail.carton_height
                pick_list_item_doc.pieces_per_carton = item_detail.pieces_per_carton
                pick_list_item_doc.finished_weight_per_unit = item_detail.finish_towel_weight
                pick_list_item_doc.finished_weight_uom = item_detail.finish_towel_weight_uom
                pick_list_item_doc.total_finished_weight = item_detail.finish_towel_weight
                pick_list_item_doc.stock_uom = item_detail.stock_uom
                pick_list_item_doc.conversion_factor = 1
                pick_list_item_doc.parent = pick_list_id
                pick_list_item_doc.parenttype = "Pick List"
                pick_list_item_doc.parentfield = "locations"
            pick_list_item_doc.insert(ignore_permissions=True)

        ducky.db.commit()
        return {"status_code": 200}

    except Exception as e:
        return {"status_code": 400}


