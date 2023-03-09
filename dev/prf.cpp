#include "cryptoTools/Crypto/AES.h"
#include "cryptoTools/Common/block.h"


using namespace oc;
using AES = oc::AES;
using u64 = oc::u64;

void prf(){
    block seed = block(123);
    AES mAes;
    mAes.setKey(seed);
    block plaintext = block(0);
    block ciphertext = mAes.ecbEncBlock(plaintext);
    std::cout << ciphertext << std::endl;
}