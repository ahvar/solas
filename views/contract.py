from flask import render_template
from flask import request
from flask.views import View, MethodView
from utility import list_pid, delete_patient_contract_pid


class ListUnpaidContractView(View):
    def dispatch_request(self):
        contracts = select_all_unpaid_patient()
        return render_template(
            "contract/list_patient_contract.html", contracts=contracts
        )


class DeleteContractByPIDView(View):
    methods = ["GET", "POST"]

    def dispatch_request(self):
        if request.method == "GET":
            pids = list_pid()
            return render_template("contract/delete_patient_contract.html", pids=pids)
        else:
            pid = int(request.form("pid"))
            result = delete_patient_contract_pid(pid)
            if result == False:
                pids = list_pid
                return render_template(
                    "contract/delete_patient_contract.html", pids=pids
                )
            contracts = select_all_patient_contract()
            return render_template(
                "contract/list_patient_contract.html", contracts=contracts
            )


class ContractView(MethodView):
    def get(self):
        return render_template("templates/contract/add_patient_contract.html")

    def post(self):
        pid = request.form["pid"]
        approver = request.form["approver"]
        result = insert_patient_contract(
            pid=int(pid),
            approved_by=approver,
            approved_date=approved_date,
            hcp=hcp,
            payment_mode=payment_mode,
            amount_paid=float(amount_paid),
            amount_due=float(amount_due),
        )
