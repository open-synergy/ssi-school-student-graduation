# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class SchoolStudentGraduationBatch(models.Model):
    """
    Extends School Student Graduation Batch with single operating unit
    support, restricting each batch record to one operating unit and
    propagating that operating unit to every school_student_graduation
    document it generates.
    """

    _name = "school_student_graduation_batch"
    _inherit = [
        "school_student_graduation_batch",
        "mixin.single_operating_unit",
    ]

    def _prepare_graduation_data(self, line):
        """Add the batch's operating unit to the graduation document data.

        Extends the base values with ``operating_unit_id`` taken from
        this batch, so every ``school_student_graduation`` record
        created from a line inherits the batch's single operating
        unit.

        :param line: ``school_student_graduation_batch_line`` record
        :return: dict of ``school_student_graduation`` values
        """
        res = super()._prepare_graduation_data(line)
        res["operating_unit_id"] = self.operating_unit_id.id
        return res
