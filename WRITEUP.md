# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

_For **both** a VM or App Service solution for the CMS app:_

- _Analyze costs, scalability, availability, and workflow_
- **_Virtual Machine_**

_Costs_

- [ ] WM typically have a higher cost and you will need to provision and manage WM hardware and software licenses, infrastructure
- [ ] You need an ongoing cost for WM storage, maintenance, security, data transfer

_Scalability_

- [ ] WM can be scaled vertically by resizing WM, that is the reason scalability in WM may be had the downtime and sometimes it would be limit because of vertical scalability
- [ ] However, WM can also be scaled horizontally by adding more instances

_Availability_

- [ ] WM requires high achieving availability by setting up redundancy, load balancing, etc. The availability of WM depended on the reliability of underlying WM infrastructure
- [ ] You will need a plan for disaster recovery and backup technologies

**_App Service_**

_Costs_

- [ ] App Service is a more cost-effective choice as it abstract infrastructure management and reducing cost
- [ ] With App Service you will have a various choice for costs by pricing plan as Free, Shared and Premium and additional service as database and storage...

_Scalability_

- [ ] App Service is scaled horizontally and we can add or remove instances easily based on demand and we don't have to be focus on significant downtime because of seamless
- [ ] App Service can be configured and handle traffic spokes automatically

_Availability_

- [ ] App Service offers built-in high availability, load balancing, and automatic failover.
- [ ] With Microsoft Azure provides a 99.95% SLA for App Service.

- _Choose the appropriate solution (VM or App Service) for deploying the app by justify your choice_

- [ ] In my solution, I will choose App Service for deploying the app because I thought, this is a small project for learning and practicing, don't necessitate more control over the infrastructure, so my demand is cost-effective, scalable, and easily manageable solution with built-in high availability and a streamlined workflow, especially for modern web applications.

### Assess app changes that would change your decision.

_Detail how the app and any other needs would have to change for you to change your decision in the last section._
I thought if the higher complexity of a CMS Application requirements which couldn't be accommodated by the constraints of Azure App Service as deep-level server configurations or OS-Level customizations, specialized software tasks, so I will lean on using WM or in the other case, our CMS application could be required exceptionally high performances that necessitate specific hardware configurations or low-level optimizations, WMs will be the better choice to handle those performances
