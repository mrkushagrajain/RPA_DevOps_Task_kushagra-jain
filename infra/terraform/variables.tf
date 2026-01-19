variable "location" {
  description = "Azure region, e.g. eastus"
  type        = string
}

variable "prefix" {
  description = "Short name prefix for resources (letters/numbers)"
  type        = string
}

variable "tags" {
  description = "Common tags"
  type        = map(string)
  default     = {}
}

variable "admin_username" {
  description = "Admin username for the VM (simulation target)"
  type        = string
}

variable "admin_ssh_key" {
  description = "Public SSH key for the VM (no secrets in code)"
  type        = string
}

variable "vm_size" {
  description = "Size for the simulated Bot Runner VM"
  type        = string
  default     = "Standard_B2s"
}
