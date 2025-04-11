# ----------------
# Permissions
# ----------------

# Assign MI access to the storage account
resource "azurerm_role_assignment" "storage_blob_contributor" {
  scope                = azurerm_storage_account.my_storage.id  
  role_definition_name = "Storage Blob Data Contributor"
  principal_id         = var.my_identity
}
