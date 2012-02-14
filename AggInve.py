# -*- encoding: utf-8 -*-

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import decimal_precision as dp
import time
import netsvc
import pooler, tools
import math
from tools.translate import _
import base64

from osv import fields, osv




class AggInvetari(osv.osv_memory):
    _name = 'gen_inventari'
    _description = 'Forza la Data del Mov = a quella dell inventario '

    
  
    def aggiorna(self, cr, uid, ids, context=None): 
        ids = context.get('active_id',False)
        if ids:
            inve_obj = self.pool.get('stock.inventory').browse(cr,uid,ids)
            if inve_obj.move_ids:
              for move in inve_obj.move_ids:
                riga = {
                        'create_date':inve_obj.date,
                        'date':inve_obj.date,
                        'date_expected':inve_obj.date,
                        }
                ok = self.pool.get('stock.move').write(cr,uid,[move.id],riga)
        
        return {'type': 'ir.actions.act_window_close'}
 

 

AggInvetari()

