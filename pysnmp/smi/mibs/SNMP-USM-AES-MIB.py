# PySNMP SMI module. Autogenerated from smidump -f python SNMP-USM-AES-MIB
# by libsmi2pysnmp-0.0.7-alpha at Mon Jul  9 17:29:49 2007,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( snmpPrivProtocols, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "snmpPrivProtocols")
( Bits, Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, TimeTicks, snmpModules, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "TimeTicks", "snmpModules")

# Objects

usmAesCfb128Protocol = MibIdentifier((1, 3, 6, 1, 6, 3, 10, 1, 2, 4))
snmpUsmAesMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 20)).setRevisions(("2004-06-14 00:00",))

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("SNMP-USM-AES-MIB", PYSNMP_MODULE_ID=snmpUsmAesMIB)

# Objects
mibBuilder.exportSymbols("SNMP-USM-AES-MIB", usmAesCfb128Protocol=usmAesCfb128Protocol, snmpUsmAesMIB=snmpUsmAesMIB)
