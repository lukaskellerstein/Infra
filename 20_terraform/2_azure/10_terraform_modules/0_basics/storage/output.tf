
# ----------------
# Output variables
# ----------------
output "storage_account_id" {
  value = azurerm_storage_account.storage.id
}

output "storage_account_name" {
  value = azurerm_storage_account.storage.name
}

output "storage_account_primary_blob_endpoint" {
  value = azurerm_storage_account.storage.primary_blob_endpoint
}

output "storage_account_primary_web_endpoint" {
  value = azurerm_storage_account.storage.primary_web_endpoint
}
