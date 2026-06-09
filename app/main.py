import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.policy import PolicyClient

# Substitua pelo ID da sua Assinatura Azure
SUBSCRIPTION_ID = "SEU_SUBSCRIPTION_ID_AQUI"
RESOURCE_GROUP_NAME = "rg-poc-governanca-free"
LOCATION = "eastus"

print("🔐 Autenticando na Azure...")
credential = DefaultAzureCredential()

resource_client = ResourceManagementClient(credential, SUBSCRIPTION_ID)
policy_client = PolicyClient(credential, SUBSCRIPTION_ID)

# 1. Criar o Grupo de Recursos da POC
print(f"📦 Criando o Grupo de Recursos: {RESOURCE_GROUP_NAME}...")
rg_result = resource_client.resource_groups.create_or_update(
    RESOURCE_GROUP_NAME,
    {"location": LOCATION}
)
print(f"✅ Grupo de Recursos criado com sucesso em {rg_result.location}")

# 2. Definir a Azure Policy para restringir tamanho de VMs (SKUs permitidas)
# Usando a definição interna (built-in) da Azure para SKUs permitidas
policy_definition_id = "/providers/Microsoft.Authorization/policyDefinitions/cccc2326-1574-4dc4-9c55-32675da9063c"

policy_assignment_parameters = {
    "listOfAllowedSKUs": {
        "value": ["Standard_B1s"] # Apenas a VM do Free Tier é permitida
    }
}

print("🛡️ Aplicando Azure Policy de restrição de tamanho de VM...")
assignment = policy_client.policy_assignments.create(
    scope=f"/subscriptions/{SUBSCRIPTION_ID}/resourceGroups/{RESOURCE_GROUP_NAME}",
    policy_assignment_name="audit-vm-size-limit",
    parameters={
        "properties": {
            "displayName": "Restringir VMs para o Free Tier (B1s)",
            "policyDefinitionId": policy_definition_id,
            "parameters": policy_assignment_parameters
        }
    }
)
print(f"✅ Azure Policy associada com sucesso! ID: {assignment.id}")
print("🚀 POC Pronta para validação manual.")