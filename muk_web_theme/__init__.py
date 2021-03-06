###################################################################################
#
#    Copyright (C) 2018 MuK IT GmbH
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

#----------------------------------------------------------
# Hooks
#----------------------------------------------------------


XML_ID = "muk_web_theme._assets_primary_variables"
SCSS_URL = "/muk_web_theme/static/src/scss/colors.scss"

def _uninstall_reset_changes(cr, registry):
    self.env['muk_utils.scss_editor'].reset_values(SCSS_URL, XML_ID)