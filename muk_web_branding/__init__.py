###################################################################################
#
#    Copyright (C) 2017 MuK IT GmbH
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

from . import models
from . import controllers

#----------------------------------------------------------
# Hooks
#----------------------------------------------------------

PRIMARY_XML_ID = "muk_web_branding._assets_primary_variables"
PRIMARY_SCSS_URL = "/muk_web_branding/static/src/scss/primary_colors.scss"

SECONDARY_XML_ID = "muk_web_branding._assets_secondary_variables"
SECONDARY_SCSS_URL = "/muk_web_branding/static/src/scss/secondary_colors.scss"

BOOTSTRAP_XML_ID = "muk_web_branding._assets_backend_helpers"
BOOTSTRAP_SCSS_URL = "/muk_web_branding/static/src/scss/bootstrap_colors.scss"

def _uninstall_rebrand_system(cr, registry):
    self.env['muk_utils.scss_editor'].reset_values(PRIMARY_SCSS_URL, PRIMARY_XML_ID)
    self.env['muk_utils.scss_editor'].reset_values(SECONDARY_SCSS_URL, SECONDARY_XML_ID)
    self.env['muk_utils.scss_editor'].reset_values(BOOTSTRAP_SCSS_URL, BOOTSTRAP_XML_ID)